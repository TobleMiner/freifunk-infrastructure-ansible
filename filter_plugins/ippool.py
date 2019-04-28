#!/usr/bin/env python

import ipaddress
import yaml
import re

class IPPool():
  IPV4 = 4
  IPV6 = 6

  def from_file(fname, poolname):
    pools = None
    with open(fname) as file:
      pools = yaml.safe_load(file)

    pool = pools[poolname]
    ranges = map(ipaddress.ip_network, pool['ranges'])

    pool_alloc = pool['allocated'] if 'allocated' in pool else { 'addresses': {}, 'networks': {} }
    alloc_addrs = { k: ipaddress.ip_address(v) for k, v in pool_alloc['addresses'].items() }
    alloc_nets = { k: ipaddress.ip_network(v) for k, v in pool_alloc['networks'].items() }

    pool_reserved = pool['reserved'] if 'reserved' in pool else []
    reserved_addrs = [ ]
    reserved_nets = [ ]

    for entry in pool_reserved:
      if '/' in entry:
        reserved_nets.append(ipaddress.ip_network(entry))
      else:
        reserved_addrs.append(ipaddress.ip_address(entry))

    return IPPool(fname, pools, poolname, ranges, alloc_addrs, alloc_nets, reserved_addrs, reserved_nets)

  def __init__(self, fname, pools, poolname, ranges, allocated_addrs, allocated_nets, reserved_addrs, reserved_nets):
    self.fname = fname
    self.pools = pools
    self.poolname = poolname
    self.ranges = ranges
    self.allocated_addrs = allocated_addrs
    self.allocated_nets = allocated_nets
    self.reserved_addrs = reserved_addrs
    self.reserved_nets = reserved_nets

  def search_net(self, prefixlen, family):
    type_addr = ipaddress.IPv4Address if family == IPPool.IPV4 else ipaddress.IPv6Address
    type_net = ipaddress.IPv4Network if family == IPPool.IPV4 else ipaddress.IPv6Network

    def filter_nets(nets):
      return filter(lambda net: type(net) == type_net, nets)

    def filter_addrs(addrs):
      return filter(lambda addr: type(addr) == type_addr, addrs)

    def ipaddr_to_octets(addr):
      clean = re.sub('/[0-9]+$', '', str(net))
      if family == IPPool.IPV4:
        return tuple(int(part) for part in clean.split('.'))
      else:
        return tuple(int(part, base=16) for part in clean.split(':'))

    candidate_nets = list(filter_nets(self.ranges))
    reserved = list(filter_nets(self.allocated_nets.values()))
    reserved.extend(filter_nets(self.reserved_nets))
    for res in reserved:
      for net in candidate_nets:
        if res.subnet_of(net):
          candidate_nets.remove(net)
          candidate_nets.extend(net.address_exclude(res))

    candidate_nets = filter(lambda net: net.prefixlen <= prefixlen, candidate_nets)
    candidate_nets = sorted(candidate_nets, key=lambda net: ipaddr_to_octets(net))
    candidate_nets = sorted(candidate_nets, key=lambda net: net.prefixlen)
    reserved = list(filter_addrs(self.allocated_addrs.values()))
    reserved.extend(self.reserved_addrs)
    for net in candidate_nets:
      for res in reserved:
        if res in net.hosts():
          break
      else:
        return next(net.subnets(prefixlen - net.prefixlen))

      break

    return None

  def _release_net(self, id):
    self.allocated_nets.pop(id)

  def _allocate_net(self, id, net):
    self.allocated_nets[id] = net

  def _save(self):
    self.pools[self.poolname].update({
      'allocated': {
        'addresses': { k: str(v) for k, v in self.allocated_addrs.items() },
        'networks': { k: str(v) for k, v in self.allocated_nets.items() },
      }
    })
    with open(self.fname, 'w') as file:
      file.write(yaml.dump(self.pools))

  def allocate_net(self, prefixlen, id, family):
    if id in self.allocated_nets:
      net = self.allocated_nets[id]
      if net.prefixlen == prefixlen:
        return net
      self._release_net(id)

    net = self.search_net(prefixlen, family)
    if not net:
      return None

    self._allocate_net(id, net)
    self._save()
    return net

def pool46(id, dom, pool, prefixlen, family):
  fname = 'ippool_{}.yml'.format(dom)
  pool = IPPool.from_file(fname, pool)

  id = "{}_{}".format(id, family)
  net = pool.allocate_net(prefixlen, id, family)

  if not net:
    raise Exception("Can't allocate IPv{} net of size {}, no space left".format(family, prefixlen))

  return str(net)

def pool4(id, dom, pool, prefixlen):
  return pool46(id, dom, pool, prefixlen, IPPool.IPV4)

def pool6(id, dom, pool, prefixlen):
  return pool46(id, dom, pool, prefixlen, IPPool.IPV6)

def ippoolid(prefix, *args):
  args = map(str, args)
  return prefix + '-'.join(args)

class FilterModule(object):
  def filters(self):
    return {
      'ippool4': pool4,
      'ippool6': pool6,
      'ippoolid': ippoolid
    }
