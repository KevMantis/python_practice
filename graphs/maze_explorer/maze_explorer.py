# Maze Explorer

# Welcome Ancient Ruins Explorer!
# We’ve identified a mysterious chamber deep underground our excavation site. The artifacts held within this chamber would be a considerable addition to the local museum…
# Unfortunately, the chamber lies at the heart of a twisted maze. We’re using a graph data structure to model the ruins. We’ll need your expertise to map out the chambers as we move through them.
# With your help, we’ll find the optimal path to the chamber before our torch burns out.

from graph import Graph, build_graph
from vertex import Vertex

# Our team has supplied you with Graph and Vertex classes, and you’ll be working from script.py.
# Tab around to get oriented, then make an excavation_site variable inside script.py and assign it to the build_graph() function we’ve supplied.
excavation_site = build_graph()

# Save your work, then type python3 script.py in the terminal to run your code.
# MAZE LAYOUT should print in the terminal.
# If your terminal ever gets too mucked up, click into the terminal and type control + l to clean it up.

# Let’s take our first steps into the maze. Tab over to graph.py.
# Inside the build_graph() function, we’ll make vertices for each room in the maze. We know there’s an entrance, so let’s start there.
# Below the line # MAKE ROOMS INTO VERTICES BELOW..., make a variable entrance and set it to an instance of Vertex with "entrance" as an argument.

# Now that we have an instance of Vertex, we need to add it to our graph.
# Below the line, # ADD ROOMS TO GRAPH BELOW..., use .add_vertex() to add entrance to graph.

# Let’s test it out.
# Save your work and run python3 script.py.
# If everything goes according to plan you should see entrance connected to... printed to the terminal.
# Congratulations, explorer. We’re ready to enter the maze…

# You bravely set foot inside the entrance and see two paths.
# After a little scouting, you identify these new rooms as an "ante-chamber" and the "king's room".
# We need to add your discoveries to build_graph().
# Make a variable ante_chamber and set it to an instance of Vertex with "ante-chamber" as the argument.
# Add the vertex, ante_chamber, to the graph.

# Make a variable kings_room and set it to an instance of Vertex with "king's room" as the argument.
# Add the vertex, kings_room, to the graph.

# Save your work and run python3 script.py.
# You should see each of the rooms listed, but they’re not connected!

# We’re using a Graph instance to track our rooms.
# Each room is a vertex. If we can travel from one room to another, that means an edge exists!
# Use the .add_edge() method within Graph to set up these connections:
# - entrance is connected to ante_chamber with a weight of 7.
# - entrance is connected to kings_room with a weight of 3.

# Save your work and run python3 script.py in the terminal. You should see the connections listed now.

# While reviewing the chambers, you discover a passage between kings_room and ante_chamber. Update the build_graph() function with this new edge.
# kings_room is connected to ante_chamber with a weight of 1.

# Emboldened by your recent discoveries, you explore deeper into the chambers.
# You unearth a grand_gallery.
# Expand our build_graph() function so it includes the variable grand_gallery set to an instance of Vertex with"grand gallery" as an argument.

# Add grand_gallery as a vertex to graph.
# Then set the edges:
# - grand_gallery is connected to ante_chamber with a weight of 2.
# - grand_gallery is connected to kings_room with a weight of 2.

# Weary but exhilarated, you come across the treasure room!
# Update build_graph() with the last chamber, make an instance of Vertex with the argument "treasure room" and assign it to the variable treasure_room.
# Add the vertex, treasure_room to the graph.

# Inside build_graph(), set the edges for the newly discovered treasure_room.
# - treasure_room is connected to ante_chamber with a weight of 6.
# - treasure_room is connected to grand_gallery with a weight of 4.

# Save your work and see the fully mapped out maze by running python3 script.py in the terminal.

# You’ve mapped out all the chambers in the maze, but in all the excitement you forgot exactly how to get to treasure_room from entrance.
# Let’s fill in the .explore() method in Graph to help you out.

# In this method, create a variable called current_room and set it equal to 'entrance'.
# Next, create a variable called path_total and set it equal to 0.

# Now create a print statement with the following text:
# "\nStarting off at the {0}\n". such that the {0} should hold the value of current_room.

# Tab back to script.py and call the .explore() method on excavation_site.
# Save your work and run python3 script.py in the terminal. The output should first map out the maze and then print "Starting off at the entrance".
excavation_site.explore()

# Now, we want to keep navigating the maze until we find the 'treasure room'. Make a while loop that checks if the current_room is NOT equal to 'treasure room'.

# In the while loop, we first want to retrieve all the data of the current_room.
# Create a variable called node and set it equal to the values corresponding to the current_room in the graph dictionary.

# After entering a room, we want to check the adjacent rooms.
# Create a for loop that iterates through the items of the node’s edges and retrieves each connected_room and weight.

# In this for loop, we will show the user all the choices of rooms they can move to and their respective costs.
# Let’s make it easy for the user and have the first letter of each room correspond to the room itself.
# In the for loop, create a variable key and set it equal to the first letter of the connected_room.

# In the for loop, print the following statement:
# "enter {0} for {1}: {2} cost"
# {0} corresponds to key. {1} corresponds to connected_room. {2} corresponds to weight.

# Outside the for loop, but still in the while loop, we want to now gather the user’s input.
# Create a variable called valid_choices and set it equal to a list of all the first letters of the keys of the node’s edges. Try using a list comprehension.

# Now, print the following:
# "\nYou have accumulated: {0} cost"
# {0} corresponds to path_total.

# Now, we want to see what room the user wants to move to.
# Create a variable choice and set it equal to the input of the following string:
# "\nWhich room do you move to? "

# Save your work and run python3 script.py in the terminal. The output should have the previous outputs and also prompt you to enter a choice.

# Now, we will check to see if the user did NOT enter valid choice.

# Back in graph.py, still within the while loop, create an if statement that checks if choice is NOT in valid_choices.
# If so, print the following:
#  - "please select from these letters: {0}"
# {0} corresponds to valid_choices.

# Now, create an else clause. This means the user selected a valid choice.
# In the else clause, create a for loop that iterates through the keys of the node’s edges and retrieves each room.

# In the for loop, create an if statement that checks if the first letter of the room is the user’s choice.
# You can use the .startswith() method.

# In the if statement, set current_room equal to the room.

# Also within the if statement, update path_total to itself plus the edge weight between the node and the room. Use the edges dictionary!

# Outside the for loop, but still within the else clause, print the following:
# "\n*** You have chosen: {0} ***\n"
# {0} corresponds to the current_room.

# Finally, outside the while loop, print the following:
# "Made it to the treasure room with {0} cost"
# {0} corresponds to the path_total.

# Congratulations! You have finished the project!
# Save your work and run python3 script.py in the terminal. Explore the maze to try and find the shortest path to the treasure!