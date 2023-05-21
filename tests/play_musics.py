import os
import sys

os.chdir(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(os.path.realpath('.'))

import argparse
import time
from pysinewave import SineWave
from utils.conversions import *
from utils.manipulation import *
from utils.player import play_pitches

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--i', type=int, default=17)
    parser.add_argument('--dt', type=float, default=0.2)
    args = parser.parse_args()

    # load musics
    with open('data/music.txt', 'r') as f:
        musics = f.readlines()
    notes = musics[args.i].split()
    
    # convert format
    pichtes = notes2pitches(notes)
    
    # play pitches
    play_pitches(pichtes, args.dt)
