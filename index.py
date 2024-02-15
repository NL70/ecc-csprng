import os
# noinspection PyUnresolvedReferences
from pyfiglet import Figlet
import numpy as np

# Seed value
seed = 0

# Curve parameters, y^2= x^3- ax + b (mod p)
p = 115792089210356248762697446949407573530086143415290314195533631308867097853951
n = 115792089210356248762697446949407573529996955224135760342422259061068512044369
a = -3
b = 0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b

# Default DUAL_EC_DRBG generator points
Px = 0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296
Py = 0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5
Qx = 0xc97445f45cdef9f0d3e05e1e585fc297235b82b5be8ff3efca67c59852018192
Qy = 0xb28ef557ba31dfcbdd21ac46e2a91e3c304f44cb87058ada2cb815151e610046

# P-256 Generator Point
Gx = 0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296
Gy = 0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5


def curve_function(x):
    global p, b, a
    return (x ** 3 - a * x + b) % p


def get_random_no(num_of_bits):
    num_of_bytes = num_of_bits // 8
    random_bytes = os.urandom(num_of_bytes)
    random_no = int.from_bytes(random_bytes, byteorder='big')
    return random_no


def generate_seed(random_no):
    global seed
    binary_rep = bin(random_no).replace("0b", "")
    if len(binary_rep) != 256:
        generate_seed(get_random_no(256))
    else:
        seed = random_no


def generate_points_on_curve():
    print("todo!")
    return 1, 2


def update_generator_points():
    global Px, Py, Qx, Qy
    Px, Py = generate_points_on_curve()
    Qx, Qy = generate_points_on_curve()


def initialisation():
    f = Figlet(font='standard')
    print(f.renderText('ECC-CSPRNG'))
    print("Welcome to ECC-CSPRNG!")
    print("Generating seed...")
    generate_seed(get_random_no(256))
    print("Seed generated!")
    if (
            input("You are currently using the default DUAL_EC_DRBG generator points. Would "
                  "you like"
                  "to generate new points? (Y/N): ").lower() == "y"):
        update_generator_points()


initialisation()
