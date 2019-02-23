def debug(val, name=None):
  if name:
    print('[DEBUG] {}: {}'.format(name, val))
  else:
    print('[DEBUG]: {}'.format(val))
  return val

class FilterModule(object):
  def filters(self):
    return {
      'debug': debug
    }
