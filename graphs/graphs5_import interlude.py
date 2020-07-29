# Import Interlude

# We’re keeping things organized by storing our classes in separate files, so let’s do a brief review on how to use code from another file.
# Python gives us the ability to import code from another file. Here’s how we can use our Vertex class from within graph.py.
#  # from <file_name> import <class>
# 
#  # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  # inside of ./vertex.py file
#  class Vertex
#    # code for the class...
#  
#  # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  # inside of ./graph.py file
#  from vertex import Vertex
#  
#  my_vertex = Vertex("Import Accomplished!")

# Use the file explorer to tab between vertex.py, graph.py, and script.py. When you’re ready to continue tab over to script.py.
# Inside of script.py, import Graph and Vertex from their respective files.
from graph import Graph
from vertex import Vertex

# Make an instance of Graph and assign it to the variable railway.
railway = Graph()

# Make an instance of Vertex with the string "Ballahoo" and assign it to the variable station.
station = Vertex("Ballahoo")

# Call .add_vertex() on railway and pass station as the argument.
railway.add_vertex(station)