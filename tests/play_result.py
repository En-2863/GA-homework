import os
import sys

os.chdir(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(os.path.realpath('.'))

import argparse
import numpy as np
from utils.conversions import *
from utils.manipulation import *
from utils.player import play_pitches

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--exp_name', type=str, default='exp_1')
    parser.add_argument('--num', type=int, default=0)
    parser.add_argument('--dt', type=float, default=0.2)
    args = parser.parse_args()

    # load results
    population = np.load(os.path.join('experiments', args.exp_name, 'final_population.npy'))
    
    # convert format
    pitches = codes2piches(population[args.num])
    
    # play pitches
    play_pitches(pitches, args.dt)
