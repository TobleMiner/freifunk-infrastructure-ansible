import hashlib

def sha256(s):
  return hashlib.sha256(str(s).encode('utf-8'))

def hashnum(s, min, max):
  return int(sha256(s).hexdigest(), 16) % (max - min) + min

def hashipv4(s):
  h = sha256(s).digest()
  parts = [ str(int.from_bytes(h[i:i + 1], 'little')) for i in range(4) ]
  return '.'.join(parts)

class FilterModule(object):
  def filters(self):
    return {
      'hashnum': hashnum,
      'hashipv4': hashipv4,
    }
