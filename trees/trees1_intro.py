# Trees Introduction

# Before we start building (planting?) our trees, let’s do a quick inventory of what we’ll need in our Python implementation. We’re going to make the class TreeNodes.
# TreeNodes:
# - have a value
# - have a reference to zero or more other TreeNodes
# - can add a node as a child
# - can remove a child
# - can traverse (or travel through) connected nodes

class TreeNode:
  def __init__(self, value):
    self.value = value
    self.children = []

  def __repr__(self, level=0):
    # HELPER METHOD TO PRINT TREE!
    ret = "--->" * level + repr(self.value) + "\n"
    for child in self.children:
      ret += child.__repr__(level+1)
    return ret

  def add_child(self, child_node):
    self.children.append(child_node) 

### TEST CODE TO PRINT TREE
company = [
  "Monkey Business CEO", 
  "VP of Bananas", 
  "VP of Lazing Around", 
  "Associate Chimp", 
  "Chief Bonobo", "Produce Manager", "Tire Swing R & D"]
root = TreeNode(company.pop(0))
for count in range(2):
  child = TreeNode(company.pop(0))
  root.add_child(child)

root.children[0].add_child(TreeNode(company.pop(0)))
root.children[0].add_child(TreeNode(company.pop(0)))
root.children[1].add_child(TreeNode(company.pop(0)))
root.children[1].add_child(TreeNode(company.pop(0)))
print("MONKEY BUSINESS, LLC.")
print("=====================")
print(root)
