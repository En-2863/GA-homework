import os
import sys

os.chdir(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(os.path.realpath('.'))

import argparse
import random
import numpy as np
from tqdm import tqdm
from utils.conversions import notes2codes
from utils.manipulation import crossOver, random_operate


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--exp_name', type=str, default='exp_1')
    parser.add_argument('--seed', type=int, default=0)
    parser.add_argument('--n_iters', type=int, default=100)
    parser.add_argument('--population', type=int, default=100)
    args = parser.parse_args()
    
    # save config
    
    os.makedirs(os.path.join('experiments', args.exp_name), exist_ok=True)
    output_file = open(os.path.join('experiments', args.exp_name, 'output.txt'), 'w')
    output_file.write(str(args) + '\n')
    
    # random seed
    
    random.seed(args.seed)
    np.random.seed(args.seed)
    
    # initialize population
    
    with open('data/music.txt', 'r') as f:
        musics = f.readlines()
    initial_population = np.stack([notes2codes(music.split()) for music in musics])
    print(f'loaded musics: {len(initial_population)}')
    
    population = np.tile(initial_population, [int(np.ceil(args.population / len(initial_population)).item()), 1])[:args.population]
    print(f'initial population: {args.population}')
    
    np.save(os.path.join('experiments', args.exp_name, 'initial_population.npy'), population)
    
    # genetic algorithm loop
    
    for step in tqdm(range(args.n_iters), desc='surviving'):
    # for step in range(args.n_iters):
        
        # augment population
        augmented_population = np.concatenate([
            population, 
            np.stack([random_operate(codes) for codes in population]), 
        ])
        indices = np.random.permutation(2 * args.population)
        parent1_indices = indices[:args.population]
        parent2_indices = indices[args.population:]
        children = np.stack([crossOver(augmented_population[parent1_indices[index]], augmented_population[parent2_indices[index]]) for index in range(args.population)])
        augmented_population = np.concatenate([augmented_population, children])
        
        # evaluate fitness
        
        
        # choose best
        population = augmented_population[np.random.choice(len(augmented_population), args.population)]
    
    # save results
    np.save(os.path.join('experiments', args.exp_name, 'final_population.npy'), population)
