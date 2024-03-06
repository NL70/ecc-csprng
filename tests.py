# noinspection PyUnresolvedReferences
from rich import print as rprint

testInt = int(open("results.txt", "r").read())
testBin = bin(testInt)[2:]


def frequency_monobit_test(bin_str):
    total = len(bin_str)
    ones = 0
    zeroes = 0
    for bit in bin_str:
        if bit == "1":
            ones += 1
        else:
            zeroes += 1
    return ones / total, zeroes / total


def run_cases():
    one_proportion, zero_proportion = frequency_monobit_test(testBin)
    print_cases(one_proportion, zero_proportion)


def print_cases(one_proportion, zero_proportion):
    rprint(f"Proportion of ones: {round(one_proportion * 100, 2)}\nProportion of zeroes: {round(zero_proportion * 100, 2)}\n")


run_cases()
