
from eccRng import ecc_rng, generate_seed, update_generator_points
from tests import run_cases
import pandas as pd
from tqdm import tqdm

bit_length = 2 ** 12
iterations = 100


def run_its():
    df = pd.DataFrame(columns=['Iteration', 'One Proportion', 'Zero Proportion', 'Invalid Blocks'])
    for i in tqdm(range(iterations)):
        generate_seed()
        update_generator_points()

        result = []
        for value in ecc_rng(int(bit_length)):
            result.append(value)
        result = int(''.join(map(str, result)))

        one_proportion, zero_proportion, invalid_blocks = run_cases(bin(result)[2:])
        new_row = pd.DataFrame(
            {'Iteration': [i+1],  'One Proportion': [one_proportion],
             'Zero Proportion': [zero_proportion],
             'Invalid Blocks': [invalid_blocks]})
        df = pd.concat([df if not df.empty else None, new_row], ignore_index=True)
    df.to_csv('test_results.csv', index=False)


run_its()
