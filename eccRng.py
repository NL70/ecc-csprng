import os
from math import floor

# import numpy as np

# Seed value
seed = 0

# Number of iterations of ec_rng
counter = 0
reseed_interval = 2 ** 36

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
    return (x ** 3 + a * x + b) % p


def point_addition(point_p, point_q):
    if point_p == "inf":
        return point_q
    if point_q == "inf":
        return point_p

    x1, y1 = point_p
    x2, y2 = point_q

    if point_p != point_q:
        # Point addition
        # Obtaining tangent through (y1-y2)/(x1-x2)
        slope = ((y2 - y1) * pow(x2 - x1, -1, p)) % p
    else:
        # Point doubling
        # Obtaining tangent through derivative of curve function
        slope = ((3 * x1 ** 2 + a) * pow(2 * y1, -1, p)) % p

    # Not sure why this works, math moment
    x3 = (slope ** 2 - x1 - x2) % p
    y3 = (slope * (x1 - x3) - y1) % p

    return x3, y3


# Double and Add algorithm
def point_multiplication(scalar, point):
    result = "inf"
    current = point

    for i in bin(scalar)[2:][::-1]:
        if i == "1":
            result = point_addition(result, current)
        current = point_addition(current, current)
    return result


def get_random_no(num_of_bits):
    num_of_bytes = num_of_bits // 8
    random_bytes = os.urandom(num_of_bytes)
    random_no = int.from_bytes(random_bytes, byteorder='big')
    return random_no


# Generates a random k where 1 <= k < n  for point multiplication
def generate_random_scalar():
    bit_length = (n.bit_length() + 7)  # Determine the number of bits needed
    while True:
        rand_int = get_random_no(bit_length)
        if 1 <= rand_int < n:
            return rand_int


def generate_seed():
    global seed
    while True:
        s = generate_random_scalar()
        binary_rep = bin(s)[2:].zfill(16)
        if len(binary_rep) == 256:
            seed = s
            break


def is_point_on_curve(point):
    x, y = point
    return curve_function(x) == (y ** 2) % p


def generate_points_on_curve():
    # Multiply generator point by k (1 to n)
    k = generate_random_scalar()
    point = point_multiplication(k, (Gx, Gy))
    return point


def update_generator_points():
    global Px, Py, Qx, Qy
    Px, Py = generate_points_on_curve()
    Qx, Qy = generate_points_on_curve()
    if is_point_on_curve((Px, Py)) and is_point_on_curve((Qx, Qy)):
        return Px, Py, Qx, Qy
    else:
        raise ValueError("Invalid points generated!")


def ecc_rng(num_of_bits):
    global counter
    s = seed
    result = []
    num_of_iterations = floor(num_of_bits / 16)
    for _ in range(int(num_of_iterations)):
        if counter >= reseed_interval:
            # rprint("Reseeding...")
            generate_seed()
            s = seed
            counter = 0

        s_p = point_multiplication(s, (Px, Py))
        r = s_p[0] % n
        r_q = point_multiplication(r, (Qx, Qy))

        random_value = r_q[0] & 0xFFFF  # Removes first 16 bits
        result.append(random_value)

        # Generating the next seed
        r_p = point_multiplication(r, (Px, Py))
        s = r_p[0] % n
        counter += 1
        yield random_value

    # concatenated_number = int(''.join(map(str, result)))
    # return concatenated_number

# TODO: Refactor code to shift all global variables to index.py,
#  then remove all calls to global variables in this
#  file so that jit can be used
# Consider replacing affine coordinates with jacobian or projective coordinates
