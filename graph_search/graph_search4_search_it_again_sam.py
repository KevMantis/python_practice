# Search It Again, Sam

# You can create a depth-first search function with a stack or with recursion (which employs a call stack). The recursive implementation is far more common, so that’s how you’ll do it here.
# Ok, roll up your sleeves and get ready to build the recursive case for your function…
# This part of the function will go something like:
'''
loop through each neighbor of the current vertex in the graph:
 
  if neighbor has not been visited:
 
    recursively call dfs on neighbor
 
    if a path exists:
 
      return the path
'''

def dfs(graph, current_vertex, target_value, visited=None):
  if visited is None:
    visited = []
  visited.append(current_vertex)
  if current_vertex == target_value:
    return visited
  # Below your base case, open a Python for loop to check each neighbor of the current_vertex in our graph.
  for neighbor in graph[current_vertex]:
    # We don’t want to revisit vertices that have already been checked, so add an if clause here that makes sure neighbor hasn’t already been added to visited.
    if neighbor not in visited:
      # Inside the if clause, set path equal to a call of dfs() with the following arguments:
      # - graph (the graph hasn’t changed)
      # - neighbor (this is the new current_vertex within the function call)
      # - target_value (the value we are still looking for)
      # - visited (now a list of at least one vertex value)
      path = dfs(graph, neighbor, target_value, visited)
      # We don’t want DFS to return None just because the first route it checked didn’t exist.
      # Check if path exists. If so, return path.
      if path:
        return path
    

the_most_dangerous_graph = {
    'lava': set(['sharks', 'piranhas']),
    'sharks': set(['lava', 'bees', 'lasers']),
    'piranhas': set(['lava', 'crocodiles']),
    'bees': set(['sharks']),
    'lasers': set(['sharks', 'crocodiles']),
    'crocodiles': set(['piranhas', 'lasers'])
  }

# Test out your DFS function!
# Outside of the function, call dfs() on the graph provided with a start vertex of "crocodiles" and a target value of "bees".
# Don’t forget to print out the result to see the path in the terminal!
print(dfs(the_most_dangerous_graph, "crocodiles", "bees"))