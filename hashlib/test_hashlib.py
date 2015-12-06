from hashlib.sha256 import test as sha256_test
from hashlib.sha512 import test as sha512_test
import hashlib

hashlib.sha224()
hashlib.sha256()
hashlib.sha384()
hashlib.sha512()

sha256_test()
sha512_test()

assert(isinstance(hashlib.new("sha224"), hashlib.sha224))
assert(isinstance(hashlib.new("sha256"), hashlib.sha256))
assert(isinstance(hashlib.new("sha384"), hashlib.sha384))
assert(isinstance(hashlib.new("sha512"), hashlib.sha512))
try:
    hashlib.new("foobar")
    assert(False)
except ValueError:
    pass

print("OK")
