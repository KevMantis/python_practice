# Tree Implementation III: Pruning

# Let’s explore how to remove nodes from a tree. Remember, child nodes are held in a list within the parent node. To remove a child, we need to remove that node from the list.
# We want the following functionality:
#  print(root.children)
#  # [child_a, child_b, child_c]
#  root.remove_child(child_b)
#  print(root.children)
#  # [child_a, child_c]
# - Call .remove_child on a specific node.
# - Pass another node as an argument
# - Remove from .children any nodes which match the argument node.

class TreeNode:
  def __init__(self, value):
    self.value = value
    self.children = []

  def add_child(self, child_node):
    print("Adding " + child_node.value)
    self.children.append(child_node)

  # Inside of the TreeNode class, define a new method remove_child, which has parameters of self and child_node. Print “Removing “ + child_node.value + “ from “ + self.value.
  def remove_child(self, child_node):
    print("Removing " + child_node.value)
    # In the body of remove_child, make a local variable, new_children, and set it to an empty list.
    new_children = []
    # Iterate through self.children and add to the new_children list any item that is not the same as the child_node argument.
    # When the iteration is over, assign self.children to be the new_children list.
    for child in self.children:
      if child != child_node:
        new_children.append(child)
    self.children = new_children

root = TreeNode("I am Root")
child = TreeNode("A wee sappling")
bad_seed = TreeNode("Root Rot!")

root.add_child(child)
root.add_child(bad_seed)

# Call remove_child on root and pass bad_seed as an argument.
root.remove_child(bad_seed)