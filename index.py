from math import floor
from time import sleep

from eccRng import ecc_rng, generate_seed, update_generator_points
# noinspection PyUnresolvedReferences
from pyfiglet import Figlet
import cProfile
# noinspection PyUnresolvedReferences
from rich import print as rprint
# noinspection PyUnresolvedReferences
from rich.console import Console

console = Console()


def initialisation():
    f = Figlet(font='standard')
    print(f.renderText('ECC-CSPRNG'))
    rprint("Welcome to ECC-CSPRNG!")
    generate_seed()
    while True:
        should_generate_points = console.input(
            "You are currently using the default DUAL_EC_DRBG generator points. Would "
            "you like"
            " to generate new points? (Y/N): ")
        if should_generate_points.lower() == "y":
            update_generator_points()
            break
        elif should_generate_points.lower() == "n":
            break

    while True:
        num_of_bits = console.input("Enter the number of bits (≥16) to generate: ")
        if num_of_bits.isdigit() and int(num_of_bits) >= 16:
            num_of_iterations = floor(int(num_of_bits) / 16)
            if (
                    console.input(
                        f"This will take {num_of_iterations} iterations. Are you sure? (Y/N): ").lower() == "y"):
                break

    profiler = cProfile.Profile()
    is_profiling = False
    while True:
        should_profile = console.input("Would you like to profile the code? (Y/N): ")
        if should_profile.lower() == "y":
            is_profiling = True
            profiler.enable()
            break
        elif should_profile.lower() == "n":
            break

    result = ecc_rng(int(num_of_bits))

    store_file = open("results.txt", "w")
    store_file.write(str(result))
    store_file.close()

    rprint(result)
    rprint("Results have been stored in results.txt")

    if is_profiling:
        profiler.disable()
        sleep(0.5)
        rprint("\nProfiling results:")
        profiler.print_stats(sort='time')

    while True:
        should_continue = console.input("\nWould you like to generate another number? (Y/N): ")
        if should_continue.lower() == "y":
            initialisation()
        elif should_continue.lower() == "n":
            rprint("Goodbye!")
            break


initialisation()
