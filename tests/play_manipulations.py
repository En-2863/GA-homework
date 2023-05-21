import os
import sys

os.chdir(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(os.path.realpath('.'))

import argparse
from utils.manipulation import *
from utils.conversions import *
from utils.player import play_pitches


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--i', type=int, default=10)
    parser.add_argument('--dt', type=float, default=0.2)
    args = parser.parse_args()

    # load musics
    with open('data/music.txt', 'r') as f:
        musics = f.readlines()
    notes = musics[args.i].split()

    # convert format
    codes = notes2codes(notes)

    # manipulate
    codes_manipulated = clamp(codes)

    # play pitches
    codes_manipulated = codes2piches(codes_manipulated)
    play_pitches(codes_manipulated, args.dt)
