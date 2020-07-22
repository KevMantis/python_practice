# Handling Collisions in the Getter

# When we retrieve hash map values, we also need to be aware of the fact that two keys could point to the same array index.

class HashMap:
  def __init__(self, array_size):
    self.array_size = array_size
    self.array = [None for item in range(array_size)]

  def hash(self, key):
    key_bytes = key.encode()
    hash_code = sum(key_bytes)
    return hash_code

  def compressor(self, hash_code):
    return hash_code % self.array_size

  def assign(self, key, value):
    array_index = self.compressor(self.hash(key))
    current_array_value = self.array[array_index]

    if current_array_value is None:
      self.array[array_index] = [key, value]
      return

    if current_array_value[0] == key:
      self.array[array_index] = [key, value]
      return

    # current_array_value currently holds different key
    return

  def retrieve(self, key):
    array_index = self.compressor(self.hash(key))
    # In our .retrieve() method, after finding the array index, we want to check to make sure that the index corresponds to the key we’re looking for.
    # Save the array value at our compressed hash code into possible_return_value.
    possible_return_value = self.array[array_index]
    # Instead of just returning the array’s contents at that index, check if possible_return_value is None. If so, return None.
    if possible_return_value == None:
      return None
    elif possible_return_value != None:
      if possible_return_value[0] == key:
        return possible_return_value[1]
    else:
      return self.array[array_index]
