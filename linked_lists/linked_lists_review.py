# Linked List Review

# Congratulations, you have implemented a linked list in Python!
# We did this by:
# -Defining a Node class to hold the values and links between nodes
# -Implementing a LinkedList class to handle external operations on the list like adding and removing nodes

# Feel free to play around a bit with your code. Here are some ideas:
# -Create a few nodes and adding them to a new linked list
# -Print your linked list out by using your stringify_list() method
# -Remove your linked list’s head node
# -Print your list again — was your original head node removed?
# -So far you’ve built a method to remove the first occurrence of a given value. How do you think you would remove all nodes that have a specific value? Try building a method to do that!
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

class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
  def get_head_node(self):
    return self.head_node
  
  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node
    
  def stringify_list(self):
    string_list = '\nlist of nodes:\n'
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + '\n'
      current_node = current_node.get_next_node()
    return string_list
  
# Only removes first instance of a given value from the linked list.
  def remove_node(self, value_to_remove):
    current_node = self.head_node
    if current_node.value == value_to_remove:
      self.head_node = current_node.next_node
    else:
      while current_node:
        current_next_node = current_node.next_node
        if not current_next_node:
          print('\nvalue \'{}\' not found'.format(value_to_remove))
          return
        elif current_next_node.value == value_to_remove:
          current_node.set_next_node(current_next_node.next_node)
          current_node = None
        else:
          current_node = current_next_node
    print('node \'{}\' removed'.format(value_to_remove))

# Removes all instances of a given value from the linked list.
  def remove_nodes(self, value_to_remove):
    node_count = self.stringify_list().count(str(value_to_remove))
    while node_count != 0:
      self.remove_node(value_to_remove)
      node_count -= 1
    print('\nall instances of \'{}\' have been removed from the linked list'.format(value_to_remove))

ll = LinkedList(5)
for n in range(10, 31, 5):
  ll.insert_beginning(n)
ll.insert_beginning(20)
ll.insert_beginning(35)
print(ll.stringify_list())
ll.remove_node(35)
print(ll.stringify_list())
ll.remove_nodes(20)
ll.remove_node(39)
print(ll.stringify_list())