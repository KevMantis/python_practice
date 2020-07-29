# Finding a Path I

# Our railway has grown to four stations with two connecting tracks. How can we tell a passenger which stations are reachable from Harwick?
#  undirected_railway = Graph()
#  
#  callan_station = Vertex('callan')
#  peel_station = Vertex('peel')
#  ulfstead_station = Vertex('ulfstead')
#  harwick_station = Vertex('harwick')
#  
#  undirected_railway.add_vertex(callan_station)
#  undirected_railway.add_vertex(peel_station)
#  undirected_railway.add_vertex(harwick_station)
#  undirected_railway.add_vertex(ulfstead_station)
#  
#  undirected_railway.add_edge(peel_station, harwick_station)
#  undirected_railway.add_edge(peel_station, callan_station)
# Our Graph class needs to determine whether a path exists between two vertices. A path means two vertices which are connected by a sequence of one or more intermediary edges and graphs.

# Define .find_path() within the Graph class.
# It takes self, start_vertex and end_vertex as arguments.
# Print that you are searching from start_vertex to end_vertex.

# Declare a start variable and assign it to a list containing start_vertex. We’ll use this list to keep track of the vertices as we search.

# Make a while loop that runs as long as start has elements inside the list.
# Inside of the while loop, declare a variable current_vertex and set it equal to the first element in start.
# You should also remove that element from start or the loop won’t terminate.
# current_vertex is the string .value property of a Vertex instance held within Graph. Inside the loop, print current_vertex.
# Tab over to script.py and run the code.

from graph import Graph
from vertex import Vertex

undirected_railway = Graph()

callan_station = Vertex('callan')
peel_station = Vertex('peel')
ulfstead_station = Vertex('ulfstead')
harwick_station = Vertex('harwick')

undirected_railway.add_vertex(callan_station)
undirected_railway.add_vertex(peel_station)
undirected_railway.add_vertex(harwick_station)
undirected_railway.add_vertex(ulfstead_station)

undirected_railway.add_edge(peel_station, harwick_station)
undirected_railway.add_edge(peel_station, callan_station)


undirected_railway.find_path('harwick', 'callan')