# host_vars
Freifunk GitHub is an example community.

One $hostname.yml for each gateway:
```yaml
---
interface:
  wan: # Uplink interface
    name: ens3 
    address:
      ipv4: 100.100.10.1

  batman:
    mac: 'de:ad:be:ef:ff:00' # batman mac for this gateway

  mesh_bridge:
    address:
      ipv4: '10.100.10.1/16' # client ipv4 address space
      ipv6: 'fd2c:2342:1337::ff00/48' # client ipv6 address space (a ula in this case)
    dhcp_range:
      start: 10.100.10.10
      end:   10.100.10.254

    ffnw:
      ipv6: 2a07:59c6:ec02:0000::1/64 # client ipv6 address space (public)

  ffnw:
    address:
      ipv4: 185.197.132.132/32 # ipv4 NAT address

mesh_vpn:
  key: # fastd keys
    private: a855738f7c860bb1a9bd23428aacb46faea1691b6f9b01788092e66d91c9e24e
    public:  df71896d986b59f34a171e546a212af2a92781e052230880a92bbed22614f87b

peering:
  ffnw:
    ber_a: # name
      transit: # transit addresses as seen from the to be deployed gateway
        local: 100.100.96.43/31
        remote: 100.100.96.42/31
    fra_a:
      transit:
        local: 100.100.32.43/31
        remote: 100.100.32.42/31

```