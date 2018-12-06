# Shamelessly stolen from https://stackoverflow.com/questions/37140846/how-to-convert-ipv6-link-local-address-to-mac-address-in-python

def lladdr(mac):
  # only accept MACs separated by a colon
  parts = mac.split(":")

  # modify parts to match IPv6 value
  parts.insert(3, "ff")
  parts.insert(4, "fe")
  parts[0] = "%x" % (int(parts[0], 16) ^ 2)

  # format output
  ipv6Parts = []
  for i in range(0, len(parts), 2):
    ipv6Parts.append("".join(parts[i:i+2]))
  ipv6 = "fe80::%s/64" % (":".join(ipv6Parts))
  return ipv6

class FilterModule(object):
  def filters(self):
    return {
      'lladdr': lladdr
    }
