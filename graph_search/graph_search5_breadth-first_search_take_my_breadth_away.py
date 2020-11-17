# Breadth-First Search: Take My Breadth Away

# Unlike DFS, BFS is primarily concerned with the shortest path that exists between two points, so that’s what we’ll be thinking about as we build out our breadth-first search function.
# Using a queue will help us keep track of the current vertex and its corresponding path. Unlike with DFS, with BFS we may have to expand on paths in several directions to find the path we’re looking for. Because of this, our path is not the same as our visited vertices.
# For visited we don’t care about the order of visitation; we only care about whether a vertex is visited or not, so we’ll use a Python set. Our breadth-first search logic should begin something like this:
'''
def bfs(graph, start_vertex, target_value):
 
  set path to a list containing the start_vertex
 
  create a queue to hold vertices and their corresponding paths
 
  define an empty visited set
'''

# Define a function bfs() with the following parameters:
# - graph (again, the graph we’re passing in)
# - start_vertex (our starting point within the graph)
# - target_value (the value we seek)
def bfs(graph, start_vertex, target_value):
  path = [start_vertex]
  #return path
#print(bfs(None, 'lava!', None))
  # Remove the return statement and the printed bfs() call.
  # Next, back inside the function, define a variable vertex_and_path as a list that contains start_vertex and our newly minted path variable.
  vertex_and_path = [start_vertex, path]
  # Where’s that queue we’re supposed to use? We’re creating it now.
  # Create a variable bfs_queue and set it equal to a list that contains vertex_and_path. We’ll use this to keep track of each vertex-path combination.
  bfs_queue = [vertex_and_path]
  # On the next line within bfs(), define visited as an empty set.
  visited = set()