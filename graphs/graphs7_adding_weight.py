# Adding Weight

# So far our Vertex class has stored edges inside of a dictionary with keys of the connected vertex’s name and the value simply set to True.
# We can make our implementation support edge weights with a few small changes. To keep this class as flexible as possible, we’ll introduce a default weight argument to .add_edge() in the Graph and Vertex classes. With no explicit weight argument, it will default to 0. We’ll then set the appropriate value in the dictionary to that weight.
# Weighted edges allow us to make graphs that represent rail systems with a travel-time between stations.
#  railway = Graph()
#  
#  callan = Vertex('callan')
#  peel = Vertex('peel')
#  harwick = Vertex('harwick')
#  
#  railway.add_vertex(callan)
#  railway.add_vertex(peel)
#  railway.add_vertex(harwick)
#  
#  # Travel-time between callan and peel: 12
#  railway.add_edge(callan, peel, 12)
#  # Travel-time between harwick and callan: 7
#  railway.add_edge(harwick, callan, 7)
#  
#  print(callan.edges)
#  # { 'peel': 12 }
#  print(harwick.edges)
#  # { 'callan': 7 }

# Inside vertex.py, alter the .add_edge() method so it takes an additional argument of weight.
# weight should default to the value of 0.

# Replace the value of True with the value of weight passed into the method.

# Tab over to graph.py.
# Inside Graph, alter .add_edge() so it also takes an additional argument of weight.
# This argument should also default to 0.

# Within the Graph class .add_edge() method, pass the weight argument to the .add_edge() methods of from_vertex and to_vertex.
# Tab over to script.py. Uncomment the code and run it.

from graph import Graph
from vertex import Vertex

railway = Graph()

callan = Vertex('callan')
peel = Vertex('peel')
harwick = Vertex('harwick')

railway.add_vertex(callan)
railway.add_vertex(peel)
railway.add_vertex(harwick)

# Uncomment the code below when you're ready to test

railway.add_edge(callan, peel, 12)
railway.add_edge(harwick, callan, 7)
railway.add_edge(peel, harwick)

print(callan.edges)
print(harwick.edges)
print(peel.edges)