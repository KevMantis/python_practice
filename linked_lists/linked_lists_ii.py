# Linked Lists Implementation II

# So far we can:
# -create a new LinkedList using .__init__()
# -get the head node of the list using .get_head_node()

# Next up, we’ll define methods for our LinkedList class that allow us to:
# -insert a new head node
# -return all the nodes in the list as a string so we can print them out in the terminal!

# We'll be using our Node class
class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

# Our LinkedList class
class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
  def get_head_node(self):
    return self.head_node

# Define an .insert_beginning() method which takes new_value as an argument.
# Inside the method, instantiate a Node with new_value. Name this new_node.
# Now, link new_node to the existing head_node.
# Finally, replace the current head_node with new_node.
  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node

# Define a .stringify_list() method we can use to print out a string representation of a list’s nodes’ values.
# The method should traverse the list, beginning at the head node, and collect each node’s value in a string. Once the end of the list has been reached, the method should return the string.
# You can use str() to convert integers to strings!
# Be sure to add "\n" between values so that each value prints on a new line.
  def stringify_list(self):
    string_list = ''
    current_node = self.get_head_node()
    while current_node:
      string_list += str(current_node.get_value()) + '\n'
      current_node = current_node.get_next_node()
    return string_list

# Test your code by uncommenting the statements below - did your list print to the terminal?
ll = LinkedList(5)
ll.insert_beginning(70)
ll.insert_beginning(5675)
ll.insert_beginning(90)
print(ll.stringify_list())