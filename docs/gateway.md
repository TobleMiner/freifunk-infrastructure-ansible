Gateway Setup
=============

Gateways that are to be used with this set of Ansible roles must be running Debian 9 (stretch).
Debian 8 (jessie) does not work and will not be supported, Debian 10 (buster) might work.

In the following documentation all occurences ```<hostname>``` are to be replaced by the name used for the gateway in the inventory file.

Gateways are defied through files placed in ```host_vars```. There must be a file ```host_vars/<hostname>.yml``` for each gateway.

An annotated example of a gateway config can be found below:

```yml
---
# network interface definition
interface:
  # definition of the primary uplink interface
  wan:
    # name of the uplink network device
    name: ens18

    # primary addresses assigned to the uplink interface
    address:
      # primary IPv4 address of the uplink interface
      ipv4: 138.201.144.216/32

  # B.A.T.M.A.N interface config
  batman:
    # MAC address of the batman interface (node_id)
    mac: 'de:ad:be:ef:ff:00'

  # configuration of the primary L2 mesh interface
  mesh_bridge:
    # Address configuration of the primary L2 mesh interface
    address:
      # IPv4 address assigned to this gateway
      ipv4: '10.116.160.1/16'

      # IPv6 address assigned to this gateway
      ipv6: 'fda1:384a:74de:4242::ff00/48'

    # Range of addresses assigned to clients by this gateway
    dhcp_range:
      start: 10.116.160.2
      end:   10.116.167.254

    # optional, required if ffnw IPv6 peering is enabled on this gateway
    ffnw:
      ipv6: 2a07:59c6:ec02:0000::1/64

  # optional, required if this gateway shall provide IPv4 exit via ffnw
  ffnw:
    address:
      # public IPv4 address assigned by ffnw, used to apply NAT to outgoing traffic
      ipv4: 185.197.132.132/32

# optional, required if mesh vpn is enabled
mesh_vpn:
  # mesh vpn private/prublic key config. PLEASE DO NOT USE THE EXAMPLE KEYS PROVIDED HERE! They are compromised.
  key:
    private: 28b0870219d3696bcfe43856bbb3ada49051c9c2201e1ffb22378503e2a8735b
    public:  0b0dd91ae88df431de13db04221ae63d4352a9b100b2c2f206b917901d83ffef

# optional, GRE + BGP peering configuration
peering:
  # peering partner specifiation, use name of institution/community you are peering with here
  ffnw:
    # peering site specification, use IATA 3-letter code + counter here (fra_a, fra_b, fra_c ...)
    ber_a:
      # transit network point to point specification, local address is assigned to local endpoint of GRE tunnel, remote address is used for BGP peering 
      transit:
        local: 100.100.96.43/31
        remote: 100.100.96.42/31

    # same as above spec
    fra_a:
      transit:
        local: 100.100.32.43/31
        remote: 100.100.32.42/31
```
