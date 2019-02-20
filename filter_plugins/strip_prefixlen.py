import re

def strip_prefix_len(cidr):
  return re.sub('\[0-9]+$', '', cidr)

class FilterModule(object):
  def filters(self):
    return {
      'strip_prefix_len': strip_prefix_len
    }
