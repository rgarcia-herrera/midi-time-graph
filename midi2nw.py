import midi
from midi.constants import NOTE_NAME_MAP_SHARP
import argparse
import networkx as nx

notes = {NOTE_NAME_MAP_SHARP[name]: name.replace('s', '#').replace('_', '')
         for name in NOTE_NAME_MAP_SHARP}

parser = argparse.ArgumentParser(
    description='plot a midi file')

parser.add_argument('music',
                    type=argparse.FileType('r'),
                    help='a midi file')

args = parser.parse_args()

pattern = midi.read_midifile(args.music)

l = pattern[1]

tracks = []

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

    if len(x) > 0:
        tracks.append((x, y))


n = 0
for track in tracks:
    G = nx.DiGraph()
    for i in range(len(track[1])-1):
        G.add_edge(notes[track[1][i]],
                   notes[track[1][i+1]])

    nx.drawing.nx_pydot.write_dot(G, "g%s.dot" % n)
    n += 1
