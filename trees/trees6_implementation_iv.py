# Tree Implementation IV: Traversing

# Our implementation has covered adding and removing nodes. Let’s expand the functionality and add the ability to move through connected nodes.
# Tree traversal is a standard operation for finding nodes with a specific value or printing all the nodes available in a tree.
# We’d like to do the following:
#  root = TreeNode('Founder')
#  child_a = TreeNode('VP of Bananas')
#  child_b = TreeNode('Executive Assistant')
#  root.add_child(child_a)
#  root.add_child(child_b)
#  root.traverse()
#  # prints "Founder", "VP of Bananas", "Executive Assistant"

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

  # Define a traverse method inside of the TreeNode class, it will only take self as an argument. Within .traverse(), print the node’s value.
  def traverse(self):
    print(self.value)
    # After printing self.value, loop through self.children and print their values. Call .traverse() on root. You should see the value of each node printed to the screen.
    for child in self.children:
      print(child.value)

root = TreeNode("CEO")
first_child = TreeNode("Vice-President")
second_child = TreeNode("Head of Marketing")

root.add_child(first_child)
root.add_child(second_child)

root.traverse()