
import hashlib


data = hashlib.sha1()
data.update(b"How about you today?")

print('Hash Value: ', data.digest())
print('Hash Value(Hex): ', data.hexdigest())

print(type(data))
print(type(data.hexdigest()))