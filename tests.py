# noinspection PyUnresolvedReferences
from rich import print as rprint
# noinspection PyUnresolvedReferences
from tqdm import tqdm
import math

test_int = int(open("results.txt", "r").read())
test_bin = bin(test_int)[2:]
block_size = 2 ** 7
p_lower_bound = 0.01  # Lower bound for p-value


def frequency_monobit_test(bin_str):
    total = len(bin_str)
    s = 0
    for bit in bin_str:
        if bit == "1":
            s += 1
        else:
            s -= 1
    p = math.erfc((abs(s) / pow(total, 0.5)) / pow(2, 0.5))
    return p


def frequency_block_test(bin_str):
    blocks = []
    p_array = []
    for i in range(0, len(bin_str), block_size):
        block = bin_str[i:i + block_size]
        blocks.append(block)

    for block in blocks:
        p_array.append(frequency_monobit_test(block))

    return p_array


def run_cases(selected_test_bin):
    p = frequency_monobit_test(selected_test_bin)
    p_array = frequency_block_test(selected_test_bin)

    invalid_blocks = 0
    for i in range(len(p_array)):
        if p_array[i] < p_lower_bound:
            invalid_blocks += 1

    invalid_blocks = invalid_blocks / len(p_array)
    # print_cases(one_proportion, zero_proportion, block_proportion, invalid_blocks)

    return p, invalid_blocks

