# A Graph Search with Real Depth

# Let’s dig into our depth-first search function and consider: what do we actually want the algorithm to do for us?
# - Find out if a path exists between vertices and return True or False accordingly?
# - Return the distance between origin and destination that we get for the first path the function finds?
# - Return the path itself?
# We’ll go with the third option here, which gives us the other information as well.
# The beginning of our depth-first function will look something like this:
'''
def dfs(graph, current_vertex, target_value, visited):
 
  set visited to empty list if not yet set
 
  add current_vertex to visited
'''

# At the top of script.py, define a function dfs that accepts the following as parameters:
# - graph (this is the graph that we pass in)
# - current_vertex (the value passed in will be the start vertex)
# - target_value (the value we are looking for)
# - visited (a list to collect the path of our algorithm) Give visited a default value of None. We won’t be passing any argument in for visited when we call the function; this parameter only exists here for the recursive calls!
def dfs(graph, current_vertex, target_value, visited=None):
  # Now we want to make sure visited gets redefined if this isn’t a recursive call.
  # 
  # Inside the function body, set visited equal to an empty list only if it’s currently equal to None.
  # Let’s test out the code. Outside the if statement, return visited and print a call of dfs(None, None, None). Did you get the empty list?
  if visited == None:
    visited = []
  # Above your return statement, add the current_vertex to the visited list — we want this to happen whether or not this is a recursive call.
  # Change the printed function call to have "bees?" as the current_vertex argument.
  visited.append(current_vertex)
  return visited

#print(dfs(None, None, None))
print(dfs(None, 'bees?', None))