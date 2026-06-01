import random
import string

length = 8

password = ''.join(random.choice(
    string.ascii_letters + string.digits)
    for i in range(length))

print("Password:", password)