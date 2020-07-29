# Introduction to Graphs

# In this lesson, we’ll build a robust implementation of the graph data structure. With just two classes, Vertex and Graph, we can implement a variety of graphs that satisfy the requirements of many algorithms.
#Let’s detail the functionality we require from these classes:
# - Vertex stores some data.
# - Vertex stores the edges to connected vertices and their weight.
# - Vertex can add a new edge to its collection.
# - Graph stores all the vertices.
# - Graph knows if it is directed or undirected.
# - Graph can add a new vertex to its collection.
# - Graph can add a new edge between stored vertices.
# - Graph can tell whether a path exists between stored vertices.
# Since we’re dealing with multiple classes, we’ll use multiple files for this implementation. To keep the concepts grounded in a real-world application, we’ll build up a transportation network of railroads and train stations as we go.

# The files vertex.py and graph.py contain the classes we’ll be building through the lesson. script.py has some utility code to build a random graph and print its vertices and edges to the console.
# Run that code a few times to see different graphs printed and continue when you’re ready.

from random import randrange
from graph1 import Graph
from vertex1 import Vertex

def print_graph(graph):
  for vertex in graph.graph_dict:
    print("")
    print(vertex + " connected to")
    vertex_neighbors = graph.graph_dict[vertex].edges
    if len(vertex_neighbors) == 0:
      print("No edges!")
    for adjacent_vertex in vertex_neighbors:
      print("=> " + adjacent_vertex)


def build_graph(directed):
  g = Graph(directed)
  vertices = []
  for val in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
    vertex = Vertex(val)
    vertices.append(vertex)
    g.add_vertex(vertex)

  for v in range(len(vertices)):
    v_idx = randrange(0, len(vertices) - 1)
    v1 = vertices[v_idx]
    v_idx = randrange(0, len(vertices) - 1)
    v2 = vertices[v_idx]
    g.add_edge(v1, v2, randrange(1, 10))

  print_graph(g)

build_graph(False)
