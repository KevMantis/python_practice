# Tree Implementation I: Planting Seeds

# Let’s start by defining our TreeNode class. We’ll begin with having our node store a value, and additional functionality can be layered on in the following exercises.

# Within script.py define an empty TreeNode class.
class TreeNode:
  # Inside the TreeNode class, define an __init__ method that takes self and value as parameters. Print “initializing node…” within __init__.
  def __init__(self, value):
    print("initializing node...")
    # Inside __init__, assign value to self.value.
    self.value = value

# Nice work! Make an instance of TreeNode and give it the value of your name as a string. Assign this to the variable: seed.
seed = TreeNode("Kevin")