from .sha256 import sha224, sha256
from .sha512 import sha384, sha512

def new(name, data=b''):
    try:
        h = {
            "sha224" : sha224,
            "sha256" : sha256,
            "sha384" : sha384,
            "sha512" : sha512,
        }[name.lower()]
    except KeyError:
        raise ValueError
    print(type(h))
    return h(data)
