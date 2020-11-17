# A Breadth of Fresh Neighbors

# We don’t want to do anything with neighbors that we’ve already visited, so we’ll skip those. Having narrowed our search down to unvisited neighboring vertices, there are two possibilities:
# - The vertex has the value we’ve been looking for.
# - The vertex doesn’t have the value we’re looking for and so we want to add it to the queue.
# Our code will follow this logic:
'''
if neighbor has not been visited:
 
  if neighbor is equal to target_value:
 
    return path including neighbor
 
  else:
 
     add neighbor and its path to the queue
'''

the_most_dangerous_graph = {
    'lava': set(['sharks', 'piranhas']),
    'sharks': set(['lava', 'bees', 'lasers']),
    'piranhas': set(['lava', 'crocodiles']),
    'bees': set(['sharks']),
    'lasers': set(['sharks', 'crocodiles']),
    'crocodiles': set(['piranhas', 'lasers'])
  }

def bfs(graph, start_vertex, target_value):
  path = [start_vertex]
  vertex_and_path = [start_vertex, path]
  bfs_queue = [vertex_and_path]
  visited = set()
  
  while bfs_queue:
    current_vertex, path = bfs_queue.pop(0)
    visited.add(current_vertex)
    for neighbor in graph[current_vertex]:
      # Inside the for loop, add an if clause that checks to be sure that neighbor is not already in our set of visited vertices.
      if neighbor not in visited:
        # Inside the if clause, create another if condition for the case that neighbor is the target_value.
        # If it is, return path with neighbor appended to it.
        if neighbor == target_value:
          return path + [neighbor]
        # Create an else condition to handle the case that we need to keep searching because neighbor is not the target_value.
        # Inside the else, append a list to bfs_queue that contains two elements:
        # - neighbor (the vertex)
        # - the path list with neighbor appended to it
        else:
          bfs_queue.append([neighbor, path + [neighbor]])

# Call bfs() on the graph in the code editor with a start vertex of “crocodiles” and a target value of “bees” and print the result!
# Is the shortest path what you expected?
print(bfs(the_most_dangerous_graph, 'crocodiles', 'bees'))