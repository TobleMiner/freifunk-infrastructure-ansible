from hashlib import sha256

def hashnum(s, min, max):
  return int(sha256(str(s).encode('utf-8')).hexdigest(), 16) % (max - min) + min

class FilterModule(object):
  def filters(self):
    return {
      'hashnum': hashnum
    }
