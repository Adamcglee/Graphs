"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex, edges = ()):
        self.vertices[vertex] = set(edges)

    def add_edge(self, start, end, undirected = True):
        self.vertices[start].add(end)
        if undirected is True:
            self.vertices[end].add(start)
