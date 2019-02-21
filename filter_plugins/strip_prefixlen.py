import re

def strip_prefixlen(cidr):
  return re.sub('/[0-9]+$', '', cidr)

class FilterModule(object):
  def filters(self):
    return {
      'strip_prefixlen': strip_prefixlen
    }
