import argparse
import time
from pysinewave import SineWave

pitch_map = {
    'c': 0, 
    '#c': 1, 
    'd': 2, 
    '#d': 3, 
    'e': 4, 
    'f': 5, 
    '#f': 6, 
    'g': 7, 
    '#g': 8, 
    'a': 9, 
    '#a': 10, 
    'b': 11, 
}

def notes2pitches(notes):
    pichtes = []
    for note in notes:
        if note == '0':
            pichtes.append('rest')
        elif note == '-':
            pichtes.append('hold')
        else:
            family = int(note[-1])
            level = pitch_map[note[:-1]]
            pichtes.append((family - 4) * 12 + level)
    return pichtes

def play_pitches(pichtes, dt):
    sinewaves = {}
    for pitch in pichtes:
        if type(pitch) == int:
            sinewaves[str(pitch)] = SineWave(pitch=pitch)
    for pitch in pichtes:
        print(pitch)
        if pitch == 'rest':
            if 'sinewave' in locals():
                sinewave.stop()
                del sinewave
        elif pitch == 'hold':
            pass
        else:
            if 'sinewave' in locals():
                sinewave.stop()
                del sinewave
            sinewave = sinewaves[str(pitch)]
            sinewave.play()
        time.sleep(dt)
    if 'sinewave' in locals():
        sinewave.stop()
        del sinewave

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
    pichtes = notes2pitches(notes)
    
    # play pitches
    play_pitches(pichtes, args.dt)
