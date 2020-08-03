# Sort a Linked List

# We also often sort data structures in order to organize the values stored in them. In this exercise, you will sort a linked list from smallest value to largest value.
# To sort a linked list, we can do the following:
# 1. Instantiate a new linked list
# 2. Find the maximum value of our inputted linked list
# 3. Insert the maximum to the beginning of the new linked list
# 4. Remove the maximum value from the inputted linked list
# 5. Repeat steps 2-4 until the head node of the inputted linked list points to None
# 6. Return the new linked list

# Fill in the sort_linked_list function such that you return a new linked list that is sorted from smallest value to largest value. Steps 1 and 5 have been completed for you.
# Use the methods in linkedlist.py and node.py to traverse, remove, and get values from the list.
# Test cases have been provided for you in order to test your code.

from linkedlist import LinkedList

def find_max(linked_list):
  current = linked_list.get_head_node()
  maximum = current.get_value()
  while current.get_next_node():
    current = current.get_next_node()
    val = current.get_value()
    if val > maximum:
      maximum = val
  return maximum

#Fill in Function
def sort_linked_list(linked_list):
  print("\n---------------------------")
  print("The original linked list is:\n{0}".format(linked_list.stringify_list()))
  new_linked_list = LinkedList()
  #Write Code Here!
  while linked_list.head_node:
    max_node_value = find_max(linked_list)
    new_linked_list.insert_beginning(max_node_value)
    linked_list.remove_node(max_node_value)
  return new_linked_list

  

#Test Cases
ll = LinkedList("Z")
ll.insert_beginning("C")
ll.insert_beginning("Q")
ll.insert_beginning("A")
print("The sorted linked list is:\n{0}".format(sort_linked_list(ll).stringify_list()))

ll_2 = LinkedList(1)
ll_2.insert_beginning(4)
ll_2.insert_beginning(18)
ll_2.insert_beginning(2)
ll_2.insert_beginning(3)
ll_2.insert_beginning(7)
print("The sorted linked list is:\n{0}".format(sort_linked_list(ll_2).stringify_list()))

ll_3 = LinkedList(-11)
ll_3.insert_beginning(44)
ll_3.insert_beginning(118)
ll_3.insert_beginning(1000)
ll_3.insert_beginning(23)
ll_3.insert_beginning(-92)
print("The sorted linked list is:\n{0}".format(sort_linked_list(ll_3).stringify_list()))

# Using the steps described in the narrative to write your sort function, what would be the big O runtime of the function? We will learn how to sort data structures with faster runtimes in future courses.
# Scroll to the bottom of the code and change the value of runtime to whichever one of these values you think the big O runtime of sort_linked_list is:
# - "1"
# - "N"
# - "log N"
# - "N log N"
# - "N^2"
# - "2^N"
# - "N!"

# Hint:
# Notice that within your loop in the sort function, you call find_max which takes O(N) time.
# If you call find_max N times, then the sort function has a runtime of O(N*N) or O(N2).

#Runtime
runtime = "N^2"
print("The runtime of sort_linked_list is O({0})\n\n".format(runtime))