# Tree Implementation V: Traversing Root to Leaf

# Our implementation of tree traversal has a slight hiccup. Trees grow many levels deep, but we’ve only accounted for one parent-child relationship.
# How is this a problem?
# 
#  root = TreeNode('Founder')
#  child_a = TreeNode('VP of Bananas')
#  child_b = TreeNode('Executive Assistant')
#  child_c = TreeNode('Banana R & D')
#
#  # adding children to the root
#  root.add_child(child_a)
#  root.add_child(child_b)
#
#  # assigning child_c to child_a creates an additional level in the tree
#  child_a.add_child(child_c)
#
#  root.traverse()
#  # prints "Founder", "VP of Bananas", "Executive Assistant"
#
# “VP of Bananas” is a child to “Founder”, and a parent to “Banana R & D”. .traverse() only goes one level deep which leaves out “Banana R & D”. Pull on your gardening gloves and let’s fix that!

class TreeNode:
  def __init__(self, value):
    self.value = value
    self.children = []

  def add_child(self, child_node):
    print("Adding " + child_node.value)
    self.children.append(child_node)
    
  def remove_child(self, child_node):
    print("Removing " + child_node.value + " from " + self.value)
    self.children = [child for child in self.children 
                     if child is not child_node]

  def traverse(self):
    print("Traversing...")
    # Inside of .traverse(), define a variable nodes_to_visit and assign it to a list containing self.
    nodes_to_visit = [self]
    # After nodes_to_visit, make a while loop that will execute as long as there are items in nodes_to_visit. Inside the body of the while loop, call .pop() on nodes_to_visit so we don’t get stuck in an infinite loop!
    while len(nodes_to_visit) > 0:
      # Inside of the while loop, make a new variable current_node and assign it to nodes_to_visit.pop().
      # Print current_node.value.
      # At the bottom of script.py, call .traverse() on root.
      current_node = nodes_to_visit.pop()
      print(current_node.value)
      # After printing current_node.value, add current_node.children to nodes_to_visit.
      # By adding a node’s children, we’ll ensure we traverse the whole tree.
      # Bask in the multi-level traversal as the whole tree is printed out!
      nodes_to_visit += current_node.children

root = TreeNode("CEO")
first_child = TreeNode("Vice-President")
second_child = TreeNode("Head of Marketing")
third_child = TreeNode("Marketing Assistant")

root.add_child(first_child)
root.add_child(second_child)
second_child.add_child(third_child)

root.traverse()
