# HashMaps vs. Linked Lists Runtime

# Dr. Shah is a busy surgeon. He sees so many different patients every day that it’s often hard to keep track which patients have which diseases. He decided to store this data in some of the cool data structures he learned about. However, because he never learnt asymptotic notation, he didn’t know which data structure would be the fastest. He decided to store his patient data in both a HashMap and a Linked List.
# In the HashMap, he stored the values as key value pairs where the patient’s name is the key and the respective patient’s disease is the value.
# In the Linked List, he made each node a list of two values: the first value is the patient’s name and the second value is the patient’s disease.
# In this exercise, you will select patient data from both the the HashMap and Linked List and compare which one is faster.

# 1. Change the value of hashmap_zachary_disease to Zachary’s disease according to the HashMap. DO NOT simply write "Sunburn Sickness". Use the HashMap methods to extract the value.

# 2. Given that N is the size of the HashMap, change the value of hashmap_runtime to the big O runtime of getting a value from a HashMap. Select from the the following options:
# - "1"
# - "N"
# - "log N"
# - "N log N"
# - "N^2"
# - "2^N"
# - "N!"

# 3. Change the value of linked_list_zachary_disease to Zachary’s disease according to the Linked List. DO NOT simply write "Sunburn Sickness". Write code that uses the Linked List and Node methods to extract the value.

# 4. Given that N is the amount of Nodes in the Linked List, change the value of linked_list_runtime to the big O runtime of getting the first value added to the Linked List. Select from the following options:
# - "1"
# - "N"
# - "log N"
# - "N log N"
# - "N^2"
# - "2^N"
# - "N!"

from hashmap import HashMap
from linkedlist import LinkedList

N = 6

#Insert Data Into HashMap
my_hashmap = HashMap(N)
my_hashmap.assign("Zachary", "Sunburn Sickness")
my_hashmap.assign("Elise", "Severe Nausea")
my_hashmap.assign("Mimi", "Stomach Flu")
my_hashmap.assign("Devan", "Malaria")
my_hashmap.assign("Gary", "Bacterial Meningitis")
my_hashmap.assign("Neeknaz", "Broken Cheekbone")

#Insert Data into LinkedList
my_linked_list = LinkedList(["Zachary", "Sunburn Sickness"])
my_linked_list.insert_beginning(["Elise", "Severe Nausea"])
my_linked_list.insert_beginning(["Mimi", "Stomach Flu"])
my_linked_list.insert_beginning(["Devan", "Malaria"])
my_linked_list.insert_beginning(["Gary", "Bacterial Meningitis"])
my_linked_list.insert_beginning(["Neeknaz", "Broken Cheekbone"])

#Get Zachary's Disease from a HashMap
hashmap_zachary_disease = my_hashmap.retrieve("Zachary") #Checkpoint 1
print("Zachary's disease is {0}".format(hashmap_zachary_disease))
hashmap_runtime = "1" #Checkpoint 2
print("The runtime of retrieving a value from a hashmap is O({0})\n\n".format(hashmap_runtime))


#Get Zachary's Disease from a Linked List
#Write Code here for Checkpoint 3
current = my_linked_list.get_head_node()
if current.value[0] == "Zachary":
  linked_list_zachary_disease = current_value[1]
else:
  while current.get_next_node() != None:
    if current.get_next_node().get_value()[0] == "Zachary":
      linked_list_zachary_disease = current.get_next_node().get_value()[1]
    current = current.get_next_node()
print("Zachary's disease is {0}".format(linked_list_zachary_disease))
linked_list_runtime = "N" #Checkpoint 4
print("The runtime of retrieving the first value added to a linked list is O({0})\n\n".format(linked_list_runtime))