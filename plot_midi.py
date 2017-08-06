import midi
import argparse
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(
    description='plot a midi file')

parser.add_argument('music',
                    type=argparse.FileType('r'),
                    help='a midi file')

args = parser.parse_args()

pattern = midi.read_midifile(args.music)

l = pattern[1]

for track in pattern:
    x = list()
    y = list()
    t = 0

    for ev in track:
        t += ev.tick
        if type(ev) == midi.events.NoteOnEvent:
            pitch, vel = ev.data
            if vel > 0:
                y.append(pitch)
                x.append(t)

    plt.plot(x, y)
plt.show()
