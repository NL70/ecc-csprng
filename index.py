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
    if (
            input("You are currently using the default DUAL_EC_DRBG generator points. Would "
                  "you like"
                  " to generate new points? (Y/N): ").lower() == "y"):
        update_generator_points()
    print(ecc_rng(10000))


initialisation()
