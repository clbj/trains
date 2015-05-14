__author__ = 'clbj'




class Dijkstra:
    def __init__(self):
        # Graph: AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7

        G = {'A': {'B': 5, 'D': 5, 'E': 7},
             'B': {'C': 4, 'x': 2},
             'C': {'D': 8, 'E': 2},
             'D': {'C': 8, 'E': 6},
             'E': {'B': 3}}
        print("Initializing")


