# Breadth-First Search 2: The Breadthening

# Phew! That was a lot of definitions at the beginning of our BFS algorithm.
# It’s time to put those shiny new variables to good use!
# Here’s the basic plan for what we’re doing:
'''
  loop through queue while the queue is not empty:
 
    set current_vertex & path equal to first vertex & path on queue
 
    add current_vertex to visited set
 
    loop through each neighbor of current_vertex in graph
'''

def bfs(graph, start_vertex, target_value):
  path = [start_vertex]
  vertex_and_path = [start_vertex, path]
  bfs_queue = [vertex_and_path]
  visited = set()
  # Below your definition of visited, start a while loop that runs as long as something is on the bfs_queue.
  while bfs_queue:
    # Inside the loop body, use Python’s so-handy-you-can’t-believe-you-didn’t-think-of-it multiple assignment to set the new variable current_vertex and path equal to the first element on bfs_queue.
    # Make sure to remove the queue element from the queue so the function doesn’t get stuck in an infinite loop!
    current_vertex, path = bfs_queue.pop(0)
    # Still inside the while loop, add current_vertex to the set of visited nodes.
    visited.add(current_vertex)
    # Now we need to look at all neighboring vertices! Just as we did with DFS, we can access this set from the graph’s value mapped to the current_vertex key.
    # Set up a for loop to iterate over each neighbor in this set of neighboring vertices.
    for neighbor in graph[current_vertex]: