# Building the Vertex

# Let’s start with our Vertex class. This class is responsible for storing information about individual vertices in our graph. In our railway network, instances of Vertex will represent train stations.
# An instance of Vertex will store data and a Python dictionary which tracks other Vertex instances connected to self.

# Inside of vertex.py, define a Vertex class. Within the Vertex class, define an __init__() method that takes self and value. Set self.value equal to value and self.edges equal to an empty dictionary.

# Define a .get_edges() method on Vertex which takes in self and returns a list of the keys of the .edges dictionary.
# .get_edges() is a convenience method which gives us a list of the names of the vertices connected to self.

# Outside the Vertex class, make an instance of Vertex with the argument "Cronk" and assign it to the variable station.

from vertex import Vertex

station = Vertex("Cronk")