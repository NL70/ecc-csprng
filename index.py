from math import floor

from eccRng import ecc_rng, generate_seed, update_generator_points
# noinspection PyUnresolvedReferences
from pyfiglet import Figlet


def initialisation():
    f = Figlet(font='standard')
    print(f.renderText('ECC-CSPRNG'))
    print("Welcome to ECC-CSPRNG!")
    print("Generating seed...")
    generate_seed()
    print("Seed generated!")
    while True:
        should_generate_points = input("You are currently using the default DUAL_EC_DRBG generator points. Would "
                  "you like"
                  " to generate new points? (Y/N): ")
        if should_generate_points.lower() == "y":
            update_generator_points()
            break
        elif should_generate_points.lower() == "n":
            break

    while True:
        num_of_bits = input("Enter the number of bits to generate: ")
        if num_of_bits.isdigit() and int(num_of_bits) > 0:
            num_of_iterations = floor(int(num_of_bits)/16)
            if (
                    input(f"This will take {num_of_iterations} iterations. Are you sure? (Y/N): ").lower() == "y"):
                break
    print(ecc_rng(int(num_of_bits)))


initialisation()
