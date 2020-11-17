# Case of Base

# Time to handle our base case!
# If the current vertex value is the same as the value we are looking for, then:
# - we’re done searching
# - we can return our path (the visited list)
# what you've built out so far:
'''
def dfs(graph, current_vertex, target_value, visited): 
 
  set visited to empty list if not yet set
 
  add current_vertex to visited
 
  # base case:
  if current_vertex is equal to target_value:
 
    return visited list
'''

def dfs(graph, current_vertex, target_value, visited=None):
  if visited == None:
    visited = []
  visited.append(current_vertex)
  # Create an if statement that returns visited when current_vertex is the same as target_value.
  if current_vertex == target_value:
    return visited