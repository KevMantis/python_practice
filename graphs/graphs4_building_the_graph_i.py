# Building the Graph I

# We’ve built a class to store information and connections between individual vertices, but we need another class that keeps track of the big picture.
# Our Graph class will track all the vertices and handle higher level concerns like whether the graph is directed, requiring edges to have a set direction, or undirected, allowing bi-directional movement across edges.
# We’ll start by giving Graph the functionality to add vertices. We’ll use an internal .graph_dict property to store every vertex by its value pointing to the vertex instance itself.
# We want to do the following:
#  grand_central = Vertex("Grand Central Station")
#  railway = Graph()
#  
#  print(railway.graph_dict)
#  # {}
#  railway.add_vertex(grand_central)
#  print(railway.graph_dict)
#  # {"Grand Central Station": grand_central}

# In graphs.py, define a Graph class with an __init__() method that takes self and directed as arguments.
# directed should default to False.
# Set directed as a property on self and set self.graph_dict to be an empty dictionary.

# In graph.py, define the .add_vertex() method on Graph. It should take self and vertex as arguments. Within the method, print “Adding “ + vertex.value.

# After the print statement, modify self.graph_dict so it has a key of the vertex‘s value pointing to the vertex itself.

# Uncomment the code to call .add_vertex() on the railway instance and pass grand_central as the argument.

from vertex import Vertex
from graph import Graph

grand_central = Vertex("Grand Central Station")

# Uncomment this code after you've defined Graph
#railway = Graph()

# Uncomment this code after you've defined Graph
railway = Graph()

# Uncomment these lines after you've completed .add_vertex()
print(railway.graph_dict)
railway.add_vertex(grand_central)
print(railway.graph_dict)