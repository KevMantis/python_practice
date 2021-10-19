# SkyRoute: A Graph Search Program

# Vancouver’s public metro system has asked you to help create a program to help commuters get from one landmark to another. You’ll be building out “SkyRoute,” a routing tool that uses breadth-first search, depth-first search, and Python dictionaries to accomplish this feat. For the purposes of this project, you can assume that it takes the same amount of time to get from each station to each of its connected neighboring stations.
# First, tab through the files you have at your disposal:
# - graph_search.py has the bfs() and dfs() functions implemented in Python
# - vc_metro.py contains a graph of all stations in the Vancouver metro system
# - vc_landmarks.py contains a dictionary of Vancouver landmarks mapped to their nearest metro station(s)
# - landmark_choices.py contains a dictionary of letters of the alphabet mapped to landmarks to make it easier for users to make a selection
# We’ve imported these for you into skyroute.py, which is where you’ll be building out the SkyRoute tool.

from graph_search import bfs, dfs
from vc_metro import vc_metro
from vc_landmarks import vc_landmarks
from landmark_choices import landmark_choices

# First, define a variable that we’ll be using throughout our program:
# landmark_string should be a string that joins all of the landmarks together, each with its corresponding letter of the alphabet from landmark_choices on a new line.
landmark_string = ''
for letter, landmark in landmark_choices.items():
  landmark_string += "{0} - {1}\n".format(letter, landmark)

# Below landmark_string, define a function greet() with no parameters. In the function body, print out two statements:
# - "Hi there and welcome to SkyRoute!"
# - "We'll help you find the shortest route between the following Vancouver landmarks:\n" + landmark_string
# See how that landmark_string already came in handy?
def greet():
  print('Hi there and welcome to SkyRoute!')
  print('We\'ll help you find the shortest route between the following Vancouver landmarks:\n' + landmark_string)

# Outside of greet(), define a new function skyroute() which will contain our full program. It won’t take any parameters. Inside, call greet().
# Great! Now, try calling skyroute() at the bottom of the file, save your code, and enter python3 skyroute.py in your console to see what happens.
def skyroute():
  greet()

skyroute()

# Let’s jump out of the skyroute() function body and define a few new functions. Add pass into the function body for each for the moment.
# - First, set_start_and_end(), which takes two parameters: start_point and end_point. This will handle setting the selected origin and destination points.
# - Next, get_start(), which takes no parameters. It will be used to request an origin from the user.
# - Finally, get_end(), which is also void of parameters. Can you guess how it will be used?
def set_start_and_end(start_point, end_point):
  pass

def get_start():
  pass

def get_end():
  pass