# A Tale of Two Graph Searches

# What time is it? Time to build out graph search algorithms in Python!
# Graph search algorithms can be tremendously helpful for path-finding between different points in a graph data structure.
# First, you’ll build out a depth-first search algorithm using recursion that can help you determine if a path exists and, if so, provide you with the first possible path that the function finds.
# Then you will build out a breadth-first search function that will lead you to the shortest path between two points.
# Are you excited? You should be. The power of graph search compels you.
# It’s possible to build graph search functions as class methods within a graph data structure implementation, but here we want to focus on the algorithms themselves. For that reason, our graphs are modeled using a Python dictionary. Within the dictionary, each key-value pair maps a vertex value to a set of that vertex’s connected vertex values:
'''
some_vertex_value: set([connected_value_1, connected_value_2, connected_value_3])
'''
# Take a look at the graphs and functions in the code editor. What do you expect the output to be when you run your code?
# Run your code to see if you were right! Now run your code again. Did the DFS path change from one run to another?

def bfs(graph, start_vertex, target_value):
  path = [start_vertex]
  vertex_and_path = [start_vertex, path]
  bfs_queue = [vertex_and_path]
  visited = set()
  while bfs_queue:
    current_vertex, path = bfs_queue.pop(0)
    visited.add(current_vertex)
    for neighbor in graph[current_vertex]:
      if neighbor not in visited:
        if neighbor is target_value:
          return path + [neighbor]
        else:
          bfs_queue.append([neighbor, path + [neighbor]])

def dfs(graph, current_vertex, target_value, visited = None):
  if visited is None:
    visited = []
  visited.append(current_vertex)
  if current_vertex is target_value:
    return visited
  
  for neighbor in graph[current_vertex]:
    if neighbor not in visited:
      path = dfs(graph, neighbor, target_value, visited)
      if path:
        return path

some_important_graph = {
    'lava': set(['sharks', 'piranhas']),
    'sharks': set(['lava', 'bees', 'lasers']),
    'piranhas': set(['lava', 'crocodiles']),
    'bees': set(['sharks']),
    'lasers': set(['sharks', 'crocodiles']),
    'crocodiles': set(['piranhas', 'lasers'])
  }

print(bfs(some_important_graph, 'lava', 'lasers'))
print(dfs(some_important_graph, 'lava', 'lasers'))