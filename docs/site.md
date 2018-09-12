Site setup
==========

In the following document all occurences of ```<site_code>``` are to be replaced by your site code (e.g. ```ffki``` for Freifunk Kiel)

A site is defined through two files. Those are:
 - A group variable definition file ```group_vars/<site_code>.yml```
 - An incentory definition file ```<site_code>```

The group variable definition will set options global to your site.
The inventory file will define all service machines used in your site (Gateways, etc.)

# Group variable definition

The group variables for your site are defined through the file ```group_vars/<site_code>.yml```. An annotated example of such a file can be found below.

```yml
---
site:
  # Your site code
  code: <site_code>

  # optional, set if your internal tld differs from your site code
  tld:  <site_code>

  # definitions concerning the mesh network wrapped inside your mesh transport
  mesh:
    network:
      # IPv4 address space of your mesh
      ipv4: 10.116.0.0/16

      # IPv6 ULA of your mesh
      ipv6: fda1:384a:74de::/48

    # optional, only needed if any of the nested options are set
    network_dynamic_clients:
      # optional, specify if you do not want to route your whole mesh ULA through the mesh interface
      ipv6: fda1:384a:74de:4242::/64

  # optional, no need to specify this if your site does not have a mesh vpn
  mesh_vpn:
    # optional, defaults to no limit, number of clients allowed to connect to this gateway
    peer_limit: 150

    # MTU of the VPN tunnel
    mtu: 1280

    # VPN port
    port: 11235

    # optional, defaults to yes, set to `no` if you want to allow nodes to connect to your vpn without registration
    verify: yes

    # git url to repository containing your fastd keys
    key_git: https://gitlab.toppoint.de/ffki/fastd-peer-keys.git

    # optional, needs to be specified only if automated updating of mesh vpn keys via ci is required, public part of key used by ci to update mesh vpn keys
    ci_deploy_key: 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDchXSfmPJsqIa1Qp0V2qtBI635BAkYedV++Gc7oKhq6EHK6c4p+B5XfwQ2nA1J/VW0b/PRVoQjGJg/vc/Y6vRB1wgce4XLHmMfTBQLGOmE6gqj/VkexHQsiU3hf1lC8QiQxaTZ6ZlmJeLP3B6vhAL1w5Is+Z+QlDYnSCinIGTeIKOHmECWdKPJrpW1SI4t1wisVy3TUZhiHwqjHIed/VgM07BdPgBmSTLfIp3FKYHGx+goi/1KtdAd4S6W/2l1wM7rtt/daaYN7QHL3Uu8xJCLJOdRkhRp1jpVN754oIO/tbT85Ax8TIR3XLDoW67Gfwt/do0rt+iUEyKe9CSJnoguGKnzSW5fUzEYOydh0u63u87Zj7Y8bjfgEEnvWFY4Vdw2Q/poDg+g5QrMH3A6uzfMiVVLM0Twm3UGKEb33RDezxZKjTv4im7SEBc3TskeRux1VVPhOukpYB0CclJoBuXigFLSzSk0MuWvu716Sm13sZv5REV/QzPaCMWURe+ITFxbeUJFH7e86we88kdwdBqrYAXZXVGMOkzfHh6l+bQQ+R/YXKfSAhepoLZywZa0uW4hmuNLt0B1xN8S+YoV/wnT6W48vNUnv5fwkY6G0MEo3F2GlAQSl0kLUFznErNbz0MylDRQ0+BwxXVHIOnxo3+bqweuFUdWrFLOQ01rGXxq4w=='

  # optional, needs to be specified if any role requiring BGP is used, AS of your site
  bgp:
    as: 65525

  # authoritative/recursive DNS server setup
  dns:
    # Configuration section of tld for your site
    <site_code>:
      # git repo containing zone files for your site tld
      git: git://git.freifunk.in-kiel.de/ffki-zone.git

      # List of dns servers used for recursing this tld
      servers:
        - 127.0.0.1@5300
        - ::1@5300

  # optional, required if you want to set up an IPv6 peering with ffnw
  ffnw:
    # network assigned by ffnw
    network:
      # ipv6 prefix assigned by ffnw
      ipv6: 2a07:59c6:ec02::/48

  # ssh repo containing ssh public keys of all administrators
  noc_keys:
    git: https://github.com/TobleMiner/ffki-noc-sshkeys.git

# B.A.T.M.A.N configuration
batman:
  # version of batman to be installed via dkms
  version: 2013.4.0-11
```


# Inventory declaration

The inventory declaration specifies all service hosts used in your setup.
The following example inventory is just what we use in in Freifunk Kiel. You will probably want to replace the hosts with your own ones

```yml
# general group containing all devices
[<site_code>]
ffki-gw0
ffki-gw6

# group containing all gateways
[gateways]
ffki-gw0
ffki-gw6

# group containg all nodes for peering with ffnw via IPv6
[peering_ffnw6]
ffki-gw0
ffki-gw6

# group containg all nodes for peering with ffnw via IPv4
[peering_ffnw4]
ffki-gw0
ffki-gw6
```
