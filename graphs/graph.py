# In graphs.py, define a Graph class with an __init__() method that takes self and directed as arguments.
# directed should default to False.
# Set directed as a property on self and set self.graph_dict to be an empty dictionary.
class Graph:
  def __init__(self, directed=False):
    self.directed = directed
    self.graph_dict = {}

  # In graph.py, define the .add_vertex() method on Graph. It should take self and vertex as arguments. Within the method, print “Adding “ + vertex.value.
  def add_vertex(self, vertex):
    print("Adding " + vertex.value)
    # After the print statement, modify self.graph_dict so it has a key of the vertex‘s value pointing to the vertex itself.
    self.graph_dict[vertex.value] = vertex

  # Within graph.py, define the .add_edge() method inside of Graph.
  # .add_edge() should take self, from_vertex, and to_vertex as arguments.
  # Print “Adding edge from from_vertex.value to to_vertex.value“
  #def add_edge(self, from_vertex, to_vertex)
  # Inside Graph, alter .add_edge() so it also takes an additional argument of weight.
  # This argument should also default to 0.
  def add_edge(self, from_vertex, to_vertex, weight=0):
    print("Adding edge from {} to {}".format(from_vertex.value, to_vertex.value))
    # In the .add_edge() method of graph.py, do the following:
    # - Key into self.graph_dict with from_vertex.value
    # - Call .add_edge on the dictionary value and pass to_vertex.value as an argument
    # Click over to vertex.py if you need a reminder of how the Vertex version of .add_edge() works.
    #self.graph_dict[from_vertex.value].add_edge(to_vertex.value)
    # Within the Graph class .add_edge() method, pass the weight argument to the .add_edge() methods of from_vertex and to_vertex.
    self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)
    # In the .add_edge() method of graph.py, if the graph is not directed, do the following:
    # - Key into self.graph_dict with to_vertex.value
    # - Call .add_edge on the dictionary value and pass from_vertex.value as an argument
    if not self.directed:
      #self.graph_dict[to_vertex.value].add_edge(from_vertex.value)
      self.graph_dict[to_vertex.value].add_edge(from_vertex.value, weight)
  
  # Define .find_path() within the Graph class.
  # It takes self, start_vertex and end_vertex as arguments.
  # Print that you are searching from start_vertex to end_vertex.
  def find_path(self, start_vertex, end_vertex):
    print("Searching from {} to {}".format(start_vertex, end_vertex))
    start =  [start_vertex]
    # Replace the commented code near start with a seen variable that begins as an empty dictionary.
    seen = {}
    # # Make a while loop that runs as long as start has elements inside the list.
    # Inside of the while loop, declare a variable current_vertex and set it equal to the first element in start.
    # You should also remove that element from start or the loop won’t terminate.
    # current_vertex is the string .value property of a Vertex instance held within Graph. Inside the loop, print current_vertex.
    while len(start) > 0:
      current_vertex = start.pop(0)
      # Replace the commented code after we declare current_vertex. Set the key of the current_vertex as True in our seen dictionary.
      seen[current_vertex] = True
      print("Visiting {}".format(current_vertex))
      # Tab over graph.py. In the while loop of the .find_path() method, check current_vertex against the given argument end_vertex.
      # If current_vertex matches the end_vertex argument, then you’ve found a path and can return True .
      if current_vertex == end_vertex:
        return True
      # Otherwise current_vertex doesn’t match, and we need to keep looking.
      # Make a new variable vertex and assign it to the vertex instance by using current_vertex to key into self.graph_dict.
      else:
        vertex = self.graph_dict[current_vertex]
        # Call .get_edges() on vertex. Assign the result to a variable called next_vertices.
        next_vertices = vertex.get_edges()
        # Change the next_vertices list, so it only includes vertices that are not in our seen dictionary.
        next_vertices = [vertex for vertex in next_vertices if vertex not in seen]
        # Add the next_vertices list to the end of start.
        # If the while loop concludes and we’ve never returned True, then we know the current_vertex never matched end_vertex. There is no path!
        # Return False after the while loop has concluded.
        start += next_vertices
    return False