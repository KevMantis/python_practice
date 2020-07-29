# Inside of vertex.py, define a Vertex class. Within the Vertex class, define an __init__() method that takes self and value. Set self.value equal to value and self.edges equal to an empty dictionary.

class Vertex:
  def __init__(self, value):
    self.value = value
    self.edges = {}

  # Define a .get_edges() method on Vertex which takes in self and returns a list of the keys of the .edges dictionary.
  # .get_edges() is a convenience method which gives us a list of the names of the vertices connected to self.
  def get_edges(self):
    edge_keys = self.edges.keys()
    return list(edge_keys)

  # Within Vertex, define the method .add_edge() that takes self, and vertex as arguments. The vertex argument will be the .value of another instance of Vertex.
  # In the body, print “Adding edge to “ + vertex.
  #def add_edge(self, vertex)
  # Inside vertex.py, alter the .add_edge() method so it takes an additional argument of weight.
  # weight should default to the value of 0.
  def add_edge(self, vertex, weight=0):
    print("Adding edge to " + vertex)
    # Use the vertex as a key within self.edges and set it to True.
    #self.edges[vertex] = True
    # Replace the value of True with the value of weight passed into the method.
    self.edges[vertex] = vertex