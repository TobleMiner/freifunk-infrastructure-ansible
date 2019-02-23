import hashlib

def sha256digest(s):
  return hashlib.sha256(str(s).encode('utf-8'))

def hashnum(s, min, max):
  return int(sha256digest(s).hexdigest(), 16) % (max - min) + min

def hashipv4(s):
  h = sha256digest(s).digest()
  parts = [ str(int.from_bytes(h[i:i + 1], 'little')) for i in range(4) ]
  return '.'.join(parts)

def sha256(s):
  return sha256digest(s).hexdigest()

class FilterModule(object):
  def filters(self):
    return {
      'hashnum': hashnum,
      'hashipv4': hashipv4,
      'sha256': sha256,
    }
