def merge(d1, d2):
  d = d1.copy()
  d.update(d2)
  return d

class FilterModule(object):
  def filters(self):
    return {
      'merge': merge
    }
