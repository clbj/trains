__author__ = 'clbj'


class Dijkstra:
    def __init__(self):
        G = {'s': {'u': 10, 'x': 5},
             'u': {'v': 1, 'x': 2},
             'v': {'y': 4},
             'x': {'u': 3, 'v': 9, 'y': 2},
             'y': {'s': 7, 'v': 6}}
        print("Initializing")


