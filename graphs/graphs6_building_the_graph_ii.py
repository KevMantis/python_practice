# Building the Graph II

# We’d like our Graph class to be able to set edges between the stored vertices. An instance of Graph is either directed or undirected, which affects how edges work between two vertices. As a reminder, the Graph class defaults to being undirected with edges being set in both directions.
# The good news is our Vertex class already has an .add_edge() method, so we can delegate most of the work.
# The Graph version of .add_edge() will take a “from” and a “to” vertex, and set the appropriate edges by calling the Vertex instance’s own .add_edge().
#  undirected_railway = Graph()
#  directed_railway = Graph(True)
#  
#  callan_station = Vertex('callan')
#  peel_station = Vertex('peel')
#  
#  undirected_railway.add_vertex(callan_station)
#  undirected_railway.add_vertex(peel_station)
#  
#  directed_railway.add_vertex(callan_station)
#  directed_railway.add_vertex(peel)
#  
#  directed_railway.add_edge(callan_station, peel_station)
#  # directed graph will set the edge one-way
#  print(callan_station.get_edges())
#  # ['peel']
#  print(peel_station.get_edges())
#  # []
#  
#  undirected_railway.add_edge(callan_station, peel_station)
#  # directed graph will set the edge both ways
#  print(callan_station.get_edges())
#  # ['peel']
#  print(peel_station.get_edges())
#  # ['callan']

# Within graph.py, define the .add_edge() method inside of Graph.
# .add_edge() should take self, from_vertex, and to_vertex as arguments.
# Print “Adding edge from from_vertex.value to to_vertex.value“
# Run the code in script.py to see your code print.

# In the .add_edge() method of graph.py, do the following:
# - Key into self.graph_dict with from_vertex.value
# - Call .add_edge on the dictionary value and pass to_vertex.value as an argument
# Click over to vertex.py if you need a reminder of how the Vertex version of .add_edge() works.
# When you’re ready, run the code in script.py

# In the .add_edge() method of graph.py, if the graph is not directed, do the following:
# - Key into self.graph_dict with to_vertex.value
# - Call .add_edge on the dictionary value and pass from_vertex.value as an argument
# Run the code in script.py

from vertex import Vertex

from graph import Graph

railway = Graph()

station_one = Vertex("Ballahoo")
station_two = Vertex("Penn")

railway.add_vertex(station_one)
railway.add_vertex(station_two)

railway.add_edge(station_one, station_two)
print("Edges for {0}: {1}".format(station_one.value, station_one.get_edges()))
print("Edges for {0}: {1}".format(station_two.value, station_two.get_edges()))