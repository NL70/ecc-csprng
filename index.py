import os
random_bytes = os.urandom(256)
seed = int.from_bytes(random_bytes, byteorder='big')
print(seed)