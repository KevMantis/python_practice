# Building the Vertex II

# We’ll continue building out the Vertex class. Remember, it’s responsible for knowing which other vertices are connected. These connections are the edges of our graph implementation.
# A key in the Vertex instance’s edges dictionary represents a connection to that other vertex. For now, we can just set the value to be True.
#  grand_central = Vertex('Grand Central Station')
#  forty_second_street = Vertex('42nd Street Station')
#  
#  print(grand_central.get_edges())
#  # []
#  
#  grand_central.add_edge(forty_second_street)
#  print(grand_central.edges)
#  # { "42nd Street Station": True }
#  print(grand_central.get_edges())
#  # ["42nd Street Station"]
# Let’s add this functionality to our Vertex class!

# Within Vertex, define the method .add_edge() that takes self, and vertex as arguments. The vertex argument will be the .value of another instance of Vertex.
# In the body, print “Adding edge to “ + vertex.

# Use the vertex as a key within self.edges and set it to True.

from vertex import Vertex

grand_central = Vertex('Grand Central Station')
forty_second_street = Vertex('42nd Street Station')

print(grand_central.get_edges())

# Use .add_edge() to assign forty_second_street.value as an edge of grand_central.
grand_central.add_edge(forty_second_street.value)

print(grand_central.get_edges())