# group_vars
Freifunk GitHub (ffgh) is an example community.

One $community_code.yml for each site:
```yaml
---
site:
  code: ffgh # code for this community
  tld:  ffgh # optinal, defaults to code
  mesh:
    network:
      ipv4: 10.100.0.0/16
      ipv6: fd2c:2342:1337::/48
    network_dynamic_clients: # optional, defaults to network.ipv6
      ipv6: fd2c:2342:1337::/64 # use if you want to assaing some static addresses

  mesh_vpn: # fastd
    peer_limit: 100 # optional, defaults to no limit
    mtu: 1280 # see https://gluon.readthedocs.io/en/v2018.1.x/user/faq.html#what-is-a-good-mtu-on-the-mesh-vpn
    key_git: https://github.com/TobleMiner/ffgh-fastd-peers.git # git for the fastd keys
    port: 11235
    verify: yes # optional, defaults to yes

  bgp:
    as: 65525 # our as number

  dns:
    ffki:
      git: git://git.freifunk.in-kiel.de/ffki-zone.git
      servers:
        - 127.0.0.1@5300
        - ::1@5300

  ffnw: # uplink provider
    network:
      ipv6: 2a07:59c6:ec02::/48 # our network

batman:
  version: 2013.4.0-11
```