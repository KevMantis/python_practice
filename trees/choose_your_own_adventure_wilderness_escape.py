# Choose Your Own Adventure: Wilderness Escape

# Welcome to Wilderness Escape, an online Choose-Your-Own-Adventure. Our users get a unique story experience by picking the next chapter of their adventure. We use the tree data structure to keep track of the different paths a user may choose. Let’s get started!

# This project will be heavily interactive.
# To get in the spirit, write a print() function inside of script.py to display “Once upon a time…” in the console.
def beginning():
  print("Once upon a time...")

beginning()

######
# TREENODE CLASS
######

# Wonderful! Our application will use the tree data structure to keep track of the different paths a user can choose in their story.
# Define a TreeNode class.
class TreeNode:
  # Our TreeNode class will keep track of two things:
  # - a portion of the story.
  # - the choices a user can make to progress in the story.
  # Within TreeNode, define an __init__() method that takes self, story_piece as arguments.
  def __init__(self, story_piece):
    # Inside of __init__(), assign story_piece to self.story_piece. Also assign self.choices to be an empty Python list.
    self.story_piece = story_piece
    self.choices = []
  
  # Every good story has a beginning, middle, and end. Let’s alter our TreeNode class so we can add the middle and end.
  # We’ll need an .add_child() method defined within TreeNode that has self and node as parameters.
  def add_child(self, node):
    # We’re treating each node in the tree as a piece of the story. It’s a Choose-Your-Own-Adventure story, so there are multiple paths the user can take.
    # Store the argument passed into add_child() inside of self.choices.
    self.choices.append(node)

  # Let’s add some functionality to our TreeNode class so we can move through the story.
  # Within TreeNode, define .traverse(). It should only take self as an argument.
  def traverse(self):
    # Inside of .traverse(), declare a variable story_node and assign it to self. This variable will track the current portion of the story.
    # Call print() with story_node.story_piece as an argument.
    story_node = self
    print(story_node.story_piece)
    # We want to take user input and progress through the story as long as there are story choices remaining.
    # Let’s break it down:
    # print out the story_node.story_piece.
    # while story_node.choices has nodes inside…
    # prompt the user for a choice.
    # set story_node to be the user’s story choice.
    # repeat until the story is over!

    # Let’s write out the while loop that will make up the rest of .traverse().
    # The loop should run as long as story_node.choices is not equivalent to an empty list.
    # If story_node.choices is an empty list then we know the story is over.
    while len(story_node.choices) > 0:
      # Inside of the while loop, declare a variable choice and set it to input() with the argument: "Enter 1 or 2 to continue the story: ".
      # This is how we will collect the user’s choice for how to progress through the story.
      choice = input("Enter 1 or 2 to continue the story: ")
      # Let’s use a conditional to ensure the user is entering valid input.
      # If choice is not in a list with the valid options, then print out a message asking them to enter a valid choice: 1 or 2.
      if choice not in ["1", "2"]:
        print("That is not a valid choice.")
      # Now let’s write the branch of the conditional where the user has made a valid choice.
      # We collected input from the terminal, so even if they entered 1, it will be a String data type. Convert it to be an Integer so we can use this choice as an index.
      # Declare a variable chosen_index and assign it to int() with choice passed as an argument.
      #chosen_index = int(choice)
      # We’re having our users enter 1 or 2, but the story_node.choices are at index 0 or 1.
      # Reassign chosen_index to be one less than it was before.
      else:
        chosen_index = int(choice) - 1
        # Declare a variable chosen_child and assign it to the appropriate choice from story_node.choices.
        # Use chosen_index to access the correct element!
        chosen_child = story_node.choices[chosen_index]
        # chosen_child is now our current portion of the story because the user selected this child node.
        # Use print() to display chosen_child.story_piece.
        print(chosen_child.story_piece)
        # Finally, set story_node to be chosen_child.
        # Our while loop will keep checking story_node to see if there are more choices to be made in our story.
        story_node = chosen_child

######
# VARIABLES FOR TREE
######

# Our market research indicates users are clamoring for a wilderness tale. Let’s get the story started…
# Declare a variable story_root and assign it to an instance of TreeNode with the following text:
# """
# You are in a forest clearing. There is a path to the left.
# A bear emerges from the trees and roars!
# Do you: 
# 1 ) Roar back!
# 2 ) Run to the left...
# """
story_root = TreeNode("""You are in a forest clearing. There is a path to the left.
A bear emerges from the trees and roars!
Do you: 
1 ) Roar back!
2 ) Run to the left...""")

# Let’s add a few more pieces of the story.
# Declare choice_a and assign it to a new instance of TreeNode with the following argument:
#  """
#  The bear is startled and runs away.
#  Do you:
#  1 ) Shout 'Sorry bear!'
#  2 ) Yell 'Hooray!'
#  """
choice_a = TreeNode("""
The bear is startled and runs away.
Do you:
1 ) Shout 'Sorry bear!'
2 ) Yell 'Hooray!'
""")

# Declare choice_b and assign it to a new instance of TreeNode with the following argument:
#  """
#  You come across a clearing full of flowers. 
#  The bear follows you and asks 'what gives?'
#  Do you:
#  1 ) Gasp 'A talking bear!'
#  2 ) Explain that the bear scared you.
#  """
choice_b = TreeNode("""
You come across a clearing full of flowers. 
The bear follows you and asks 'what gives?'
Do you:
1 ) Gasp 'A talking bear!'
2 ) Explain that the bear scared you.)
""")

# Call add_child() on story_root and pass choice_a as an argument.
story_root.add_child(choice_a)

# Call add_child() on story_root and pass choice_b as an argument.
story_root.add_child(choice_b)

# Wonderful! Now our story has a beginning in the variable story_root, and two choices available for a middle section stored inside of story_root.choices.

# Our functionality is all in place, all we have left to do is finish the story. Let’s create the child nodes for choice_a.
# Declare a variable choice_a_1 and assign it to an instance of TreeNode with the following string as an argument:
# """
# The bear returns and tells you it's been a rough week. After making peace with
# a talking bear, he shows you the way out of the forest.
# 
# YOU HAVE ESCAPED THE WILDERNESS.
# """
choice_a_1 = TreeNode("""
The bear returns and tells you it's been a rough week. After making peace with
a talking bear, he shows you the way out of the forest.

YOU HAVE ESCAPED THE WILDERNESS.
""")

# Declare a variable choice_a_2 and assign it to an instance of TreeNode with the following string as an argument:
# """
# The bear returns and tells you that bullying is not okay before leaving you alone
# in the wilderness.
# 
# YOU REMAIN LOST.
# """
choice_a_2 = TreeNode("""
The bear returns and tells you that bullying is not okay before leaving you alone
in the wilderness.

YOU REMAIN LOST.
""")

# choice_a_1 and choice_a_2 should be child nodes to choice_a.
# Call .add_child() on choice_a to set up the relationship between these nodes.
choice_a.add_child(choice_a_1)
choice_a.add_child(choice_a_2)

# Click “Save” and in the terminal run python3 script.py. Navigate through these new sections of the story.

# Now let’s create the child nodes for choice_b.
# Declare a variable choice_b_1 and assign it to an instance of TreeNode with the following string as an argument:
# """
# The bear is unamused. After smelling the flowers, it turns around and leaves you alone.
# 
# YOU REMAIN LOST.
# """
choice_b_1 = TreeNode("""
The bear is unamused. After smelling the flowers, it turns around and leaves you alone.

YOU REMAIN LOST.
""")

# Declare a variable choice_b_2 and assign it to an instance of TreeNode with the following string as an argument:
# """
# The bear understands and apologizes for startling you. Your new friend shows you a 
# path leading out of the forest.
# 
# YOU HAVE ESCAPED THE WILDERNESS.
# """
choice_b_2 = TreeNode("""
The bear understands and apologizes for startling you. Your new friend shows you a 
path leading out of the forest.

YOU HAVE ESCAPED THE WILDERNESS.
""")

# Set up the appropriate relationship for choice_b_1 and choice_b_2; they should be child nodes of choice_b.
choice_b.add_child(choice_b_1)
choice_b.add_child(choice_b_2)

######
# TESTING AREA
######

# Test out that we’re on the right path by printing story_root.story_piece near the bottom of script.py.
# In the terminal, run python3 script.py.
# print(story_root.story_piece)

# A Choose-Your-Own-Adventure wouldn’t be any fun if it weren’t interactive. Let’s explore how we can take input from the user. Outside of the TreeNode class, declare a variable user_choice and assign it to input("What is your name? ")
#user_choice = input("What is your name? ")

# Immediately below input(), print out user_choice and click “Save”.
#print(user_choice)

# Inside of the terminal type python3 script.py to run our program.
# You should see the argument given to input(), “What is your name? “, printed to the screen.
# The terminal is waiting for your response. Type in your name and press the enter key.

# Did you see your name printed out?
# This is how users will progress through our Choose-Your-Own-Adventure, they’ll enter a number to select one of the displayed choices.
# Experiment a few times typing in different things. Comment out or delete those lines of code so they don’t run and clutter up the terminal.

# Test out our .traverse() method by calling it on story_root.
# Click “Save” and run our script by typing python3 script.py in the terminal.
# You should see the beginning of the story printed out.
#story_root.traverse()

# Congratulations! We have a functioning Choose-Your-Own-Adventure.
# At the bottom of script.py, call .traverse() on story_root.
# Click “Save”, and run python3 script.py in the terminal.
# You should be able to progress through one level of the story!
story_root.traverse()