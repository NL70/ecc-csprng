# noinspection PyUnresolvedReferences
from rich import print as rprint
# noinspection PyUnresolvedReferences
from tqdm import tqdm
from time import sleep

testInt = int(open("results.txt", "r").read())
testBin = bin(testInt)[2:]
block_prop_min = 0.40  # min acceptable percentage of ones in each block
block_prop_max = 0.60  # Max acceptable percentage of ones in each block


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


def frequency_block_test(bin_str):
    block_size = 128
    blocks = []
    proportion = []
    for i in range(0, len(bin_str), block_size):
        block = bin_str[i:i + block_size]
        blocks.append(block)

    for block in blocks:
        ones = block.count('1')
        proportion.append(ones / len(block))

    return proportion


def run_cases():
    one_proportion, zero_proportion = frequency_monobit_test(testBin)
    block_proportion = frequency_block_test(testBin)
    print_cases(one_proportion, zero_proportion, block_proportion)


def print_cases(one_proportion, zero_proportion, block_proportion):
    rprint(f"Checking total proportion of ones and zeroes...")
    rprint(
        f"Proportion of ones: {round(one_proportion * 100, 2)}\nProportion of zeroes: {round(zero_proportion * 100, 2)}")
    rprint("\nChecking proportion of ones in each block...")

    invalid_blocks = 0
    for i in range(len(block_proportion)):
        if not (block_prop_min < round(block_proportion[i], 2) < block_prop_max):
            # rprint("Invalid block!")
            # rprint(f"Block {i + 1}: {round(block_proportion[i], 2)}")
            invalid_blocks += 1
    rprint(f"Percentage of invalid blocks: {round((invalid_blocks / len(block_proportion)*100), 2)}")
    rprint(f"Upper bound for % of ones: {block_prop_max*100}")
    rprint(f"Lower bound for % of ones: {block_prop_min*100}")


run_cases()
