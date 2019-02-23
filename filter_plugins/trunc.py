def trunc(s, len):
  return s[:len]

class FilterModule(object):
  def filters(self):
    return {
      'trunc': trunc
    }
