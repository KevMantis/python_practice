# Tree Implementation II: Think of the Children

# We have a working TreeNode class, but there’s no time to enjoy a refreshing glass of lemonade. Trees are all about data hierarchy, and we need a parent-child relationship to make that work.
# To review: child nodes are held as references by another instance of TreeNode, known as the parent node.
#  parent = TreeNode('CEO')
#  child = TreeNode('Executive Assistant')
#  print(parent.children)
#  # []
#  parent.add_child(child)
#  print(parent.children)
#  # [child]
# We’ll store the references to child nodes in a Python list and define an add_child method on our TreeNode class which will add nodes to that list.

class TreeNode:
  def __init__(self, value):
    self.value = value
    # Modify our __init__ method by setting self.children to be an empty list.
    self.children = []
  
  # Define add_child on the TreeNode class. It should take self and child_node as parameters. In the body of add_child, start with print("Adding " + child_node.value).
  def add_child(self, child_node):
    print("Adding " + child_node.value)
    # After the print statement, use a list method to add the child_node to self.children.
    self.children.append(child_node)

root = TreeNode("I am Root")
child = TreeNode("A wee sappling")

# Finally, call add_child on root and pass child as an argument.
root.add_child(child)