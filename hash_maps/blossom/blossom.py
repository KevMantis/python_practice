# Blossom

# The language of the flowers has a long history and has often been a topic resigned to the domain of dusty books in a thrift bookseller or a library. With Blossom, we want to give people lightning fast access to all of the possible meanings of their favorite flowers.
# In this project, we are going to implement a hash map to relate the names of flowers to their meanings. In order to avoid collisions when our hashing function collides the names of two flowers, we are going to use separate chaining. We will implement the Linked List data structure for each of these separate chains.

# The underlying data structure for Blossom is going to be a key-value store that uses the common names for flowers as the key and saves the floral meaning of the flower as the value.
# In order to implement this functionality, we’re going to build out a hash map with separate chains of linked lists at every index.
# First, let’s define our HashMap class.

# Let’s add in the separate chaining aspect of our algorithm. Import the linked list and node library by calling
#  from linked_list import Node, LinkedList
# At the top of script.py
from linked_list import Node, LinkedList

class HashMap:
  # The first thing that we’ll need for our hash map is an array. Python’s lists behave similar to an array, but we’ll need to keep track and enforce the list’s size to make the resemblance stronger.
  # Give HashMap a constructor that takes a size parameter. Save size into self.array_size.
  # After that, create a list of None objects of length size and save it into self.array.
  def __init__(self, size):
    self.array_size = size
    #self.array = [None for item in range(size)]
    # In HashMap.__init__, find the line where we created a list of None objects.
    # Change this so that self.array instead is a list of LinkedLists.
    # The resulting self.array should be a Python list of LinkedList objects, make sure to instantiate them.
    self.array = [LinkedList() for item in range(size)]

  # In order to implement a hash map, we need to implement four different methods.
  # The first two are the internal methods needed to perform the basic responsibilities of a hash map: .hash() and .compress().
  # The next two are the external methods someone interacting with the hash map will use: .assign() and .retrieve().
  # Let’s start by implementing a basic hash function. When the key is a string (which is true for all of Blossom’s keys) we’ll need to calculate a number for that string. Let’s sum up the character encodings of each character in the string and use that.
  # Define a method called .hash() that takes both self and key as parameters.
  def hash(self, key):
    # Calculate the hash code for the key by calling key.encode() and performing the sum on the resulting list-like object.
    return sum(key.encode())

  # Now that we have a hash function, that returns a number, we’ll also need a compression function that reduces this number into an array index.
  # Define a .compress() method that takes a hash_code parameter. Return the result of calculating the remainder of dividing hash_code by self.array_size.
  def compress(self, hash_code):
    return hash_code % self.array_size

  # With our hash and compression functions written, all we need to create a basic hash map are our .assign() and .retrieve() methods. Let’s start with .assign().
  # Define a .assign() method that takes three parameters: self, key, and value. Get the hash code by plugging key into .hash() and then get the array index by plugging the resulting hash code into .compress(). Save the result into the variable array_index.
  def assign(self, key, value):
    array_index = self.compress(self.hash(key))
    # In the array, at the address array_index, save both the key and the value as a list: [key, value].
    #self.array[array_index] = [key, value]

    # In .assign(), we’re going to be replacing the assign logic after getting the array_index from the .hash() and .compressor() methods.
    # Create a new Node object with value [key, value]. Assign that Node object to a variable called payload.
    payload = Node([key, value])
    # We’ll need to check if the key exists in the LinkedList before we add our new payload to it. Save self.array[array_index] into the variable list_at_array.
    list_at_array = self.array[array_index]
    # Iterate through list_at_array using a for loop. For every item in list_at_array, check if the key (the element at index 0) is the same as the key we’re trying to assign.
    for i in list_at_array:
      if i[0] == key:
        # If we do find a key at one of the items in the linked list, overwrite its value with value.
        i[1] = value
        return
    # If we’ve iterated through the list and not found our key, we need to add it.
    # Remove the line where we assign
    #  self.array[array_index] = [key, value]
    # And change it so that we use list_at_array.insert() to insert the payload to our chained list.
    list_at_array.insert(payload)
  
  # .retrieve() should find the hash code for key by plugging it into .hash() and then find the array index by plugging that hash code into .compress().
  # Save that index into a variable called array_index
  def retrieve(self, key):
    array_index = self.compress(self.hash(key))
    # Save the value of self.array at array_index into a variable called payload.
    #payload = self.array[array_index]

    # Now we’re going to update .retrieve() to use separate chaining. We’re going to rewrite the code after we get our array_index.
    # Using the array_index variable, get the LinkedList object at that index in self.array. Before we called this payload but since it represents a different type of object, let’s name it something different.
    # Save the result into a variable called list_at_index.
    list_at_index = self.array[array_index]

    # If payload is not None, then we know it’s a list that looks like [key, value].
    # Check the first item (payload[0]) and compare it with key. If they are the same, return the second item in payload (the value!).
    # If payload is None or the first item is not the same as key, return None.
    #if payload[0] == key:
      #return payload[1]
    #if payload is None or payload[0] != key:
      #return None

    # Iterate through the linked list similarly to how .assign() did, checking the key in each part of the list to see if it’s the same as our key.
    for i in list_at_index:
      if i[0] == key:
        # If you do find the key, return the value (at index 1 in the node’s value), otherwise return None!
        return i[1]
    return None

# Now lets add in some flower definitions! Use
#  from blossom_lib import flower_definitions 
# To import the flower definitions.
from blossom_lib import flower_definitions

# Now let’s create a new instance of our HashMap create an instance called blossom. Make the list of our new HashMap the same length as flower_definitions.
blossom = HashMap(len(flower_definitions))

# Now, for every element of flower_definitions, assign the value (index 1) to its key (index 0) using blossom.assign().
for flower in flower_definitions:
  blossom.assign(flower[0], flower[1])

# Now use our app! Look up a flower’s meaning using blossom.retrieve('daisy'). Try printing it out!
# Does it work? Next, try looking up another flower. Is the flower you’re looking for missing? How would you add it in?
print(blossom.retrieve("daisy"))