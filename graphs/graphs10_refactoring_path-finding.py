# Refactoring Path-Finding

# Our pathfinding method works when a path exists, but there is a serious bug! We’re not accounting for cycles in our graph.
# Consider the following undirected Graph:
#  railway = Graph()
#  
#  callan = Vertex('callan')
#  peel = Vertex('peel')
#  ulfstead = Vertex('ulfstead')
#  harwick_station = Vertex('harwick')
#  
#  railway.add_vertex(callan)
#  railway.add_vertex(peel)
#  railway.add_vertex(harwick)
#  railway.add_vertex(ulfstead)
#  
#  railway.add_edge(peel, harwick)
#  railway.add_edge(harwick, callan)
#  railway.add_edge(callan, peel)
#  
#  railway.find_path(peel, ulfstead)
# Peel connects to Harwick and Callan. We look for a path starting at peel, adding harwick and callan to the start list. Next, we look at harwick, adding peel and callan. We’ll keep adding the same vertices, and our loop will never terminate.
# When a path exists, return True will exit the loop. When a path does not exist, it’s a major problem!
# We’ll use a dictionary to track which stations we’ve visited. This will stop our passengers from riding around in circles.

# Replace the commented code near start with a seen variable that begins as an empty dictionary.

# Replace the commented code after we declare current_vertex. Set the key of the current_vertex as True in our seen dictionary.

# Replace the commented code before we add to the start list.

# Change the next_vertices list, so it only includes vertices that are not in our seen dictionary.

# Test out our improved .find_path() method!

# Tab over to script.py, uncomment the relevant code and run our script.

from graph import Graph
from vertex import Vertex

railway = Graph()

callan = Vertex('callan')
peel = Vertex('peel')
ulfstead = Vertex('ulfstead')
harwick = Vertex('harwick')

railway.add_vertex(callan)
railway.add_vertex(peel)
railway.add_vertex(harwick)
railway.add_vertex(ulfstead)

railway.add_edge(peel, harwick)
railway.add_edge(harwick, callan)
railway.add_edge(callan, peel)

# Uncomment the code below when you're done refactoring!

peel_to_ulfstead_path_exists = railway.find_path('peel', 'ulfstead')
harwick_to_peel_path_exists = railway.find_path('harwick', 'peel')

print("A path exists between peel and ulfstead:")
print(peel_to_ulfstead_path_exists)
print("A path exists between harwick and peel:")
print(harwick_to_peel_path_exists)