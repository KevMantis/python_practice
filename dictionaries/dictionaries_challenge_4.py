# Values That Are Keys

# Create a function named values_that_are_keys that takes a dictionary named my_dictionary as a parameter. This function should return a list of all values in the dictionary that are also keys.
def values_that_are_keys(my_dictionary):
  new_list = []
  for value in my_dictionary.values():
    if value in my_dictionary.keys():
      new_list.append(value)
  return new_list

print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))

print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))