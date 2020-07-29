# Finding a Path II

# Our pathfinding method is almost complete. Let’s take a step back and think how a passenger in Harwick station could find their way to Callan.
# First, they’d look for all the stations connected to Harwick. If one of those stations was Callan, they’re in luck!
# Otherwise, they would look for the connections from each of those stations excluding Harwick because they’ve already crossed it off their list.
# We’ll take the same strategy with our pathfinding method.
#  while len(start) > 0:
#    current_vertex = start.pop(0)
#    # current_vertex is end_vertex
#      # a path exists!
#    # current_vertex is not end_vertex
#      # add vertices connected to 
#      # current_vertex onto the list
#      # to keep searching for a path

# Tab over graph.py. In the while loop of the .find_path() method, check current_vertex against the given argument end_vertex.
# If current_vertex matches the end_vertex argument, then you’ve found a path and can return True .
# Tab over to script.py and run the code.

# Otherwise current_vertex doesn’t match, and we need to keep looking.
# Make a new variable vertex and assign it to the vertex instance by using current_vertex to key into self.graph_dict.

# Call .get_edges() on vertex. Assign the result to a variable called next_vertices.

# Add the next_vertices list to the end of start.
# If the while loop concludes and we’ve never returned True, then we know the current_vertex never matched end_vertex. There is no path!
# Return False after the while loop has concluded.
# Go to script.py. Uncomment and run the code.

from graph import Graph
from vertex import Vertex

no_path_exists = True


directed_railway = Graph(True)

callan_station = Vertex('callan')
peel_station = Vertex('peel')
ulfstead_station = Vertex('ulfstead')
harwick_station = Vertex('harwick')

directed_railway.add_vertex(callan_station)
directed_railway.add_vertex(peel_station)
directed_railway.add_vertex(harwick_station)
directed_railway.add_vertex(ulfstead_station)

directed_railway.add_edge(harwick_station, peel_station)
directed_railway.add_edge(peel_station, callan_station)


path_exists = directed_railway.find_path('harwick', 'harwick')
print(path_exists)

#Uncomment for final checkpoint

print("\n\n\nFinding path from harwick to callan\n")
new_path_exists = directed_railway.find_path('harwick', 'callan')
print(new_path_exists)
print("\n\nTrying to find path from harwick to ulfstead\n")
no_path_exists = directed_railway.find_path('harwick', 'ulfstead')
print(no_path_exists)