
import hashlib

word = "How about you today?"
data = hashlib.md5()
data.update(word.encode())

print('Hash Value: ', data.digest())
print('Hash Value(Hex): ', data.hexdigest())

print(type(data))
print(type(data.hexdigest()))

cword = "你今天好嗎?"
data = hashlib.md5()
data.update(cword.encode('utf-8'))

print('Hash Value: ', data.digest())
print('Hash Value(Hex): ', data.hexdigest())

print(type(data))
print(type(data.hexdigest()))