# Tree Implementation IIIa: Tuning the Pruning

# Trees are an abstract idea that we’re making concrete in Python. When implementing these abstract data structures, it’s important to leverage the features of your language.
# Let’s refactor .remove_child() to use Python’s list comprehension. As a quick refresher on list comprehension:
#  nums = [1, 2, 3, 4, 5]
#  evens = [num for num in nums if num % 2 == 0]
#  # [2, 4]

class TreeNode:
  def __init__(self, value):
    self.value = value
    self.children = []

  def add_child(self, child_node):
    print("Adding " + child_node.value)
    self.children.append(child_node)
    
  def remove_child(self, child_node):
    print("Removing " + child_node.value + " from " + self.value)
    # Replace the existing code in .remove_child and assign self.children to a list comprehension which performs the same logic.
    #new_children = []
    #for child in self.children:
    #  if child != child_node:
    #    new_children.append(child)
    #self.children = new_children
    self.children = [child for child in self.children if child != child_node]

root = TreeNode("I am Root")
child = TreeNode("A wee sappling")
bad_seed = TreeNode("Root Rot!")

root.add_child(child)
root.add_child(bad_seed)

root.remove_child(bad_seed)