import midi
import argparse
import networkx as nx
from pprint import pprint
import matplotlib.pyplot as plt


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


G = nx.DiGraph()

for track in tracks:
    for i in range(len(track[1])-1):
        G.add_edge(track[1][i], track[1][i+1], t=track[0][i+1]-track[0][i])

    nx.draw_networkx(G)
    plt.show()
