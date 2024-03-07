from eccRng import ecc_rng, generate_seed, update_generator_points
from tests import run_cases
import pandas as pd
from tqdm import tqdm
from concurrent.futures import ProcessPoolExecutor

bit_length = 2 ** 12
iterations = 1000


def run_single_it(i):
    generate_seed()
    update_generator_points()

    result = []
    for value in ecc_rng(int(bit_length)):
        result.append(value)
    result = int(''.join(map(str, result)))

    p, invalid_blocks = run_cases(bin(result)[2:])
    new_row = pd.DataFrame(
        {'Iteration': [i + 1], 'p': [p],
         'Invalid Blocks': [invalid_blocks]})
    return new_row


def run_its():
    df = pd.DataFrame(columns=['Iteration', 'One Proportion', 'Zero Proportion', 'Invalid Blocks'])
    with ProcessPoolExecutor() as executor:
        for i, new_row in enumerate(tqdm(executor.map(run_single_it, range(iterations)), total=iterations)):
            df = pd.concat([df if not df.empty else None, new_row], ignore_index=True)
            df.to_csv('test_results.csv', index=False)



if __name__ == '__main__':
    run_its()
