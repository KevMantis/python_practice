# Largest Value

# Write a function named max_key that takes a dictionary named my_dictionary as a parameter. The function should return the key associated with the largest value in the dictionary.
def max_key(my_dictionary):
  largest_key = ''
  largest_value = float('-inf')
  for key, value in my_dictionary.items():
    if value > largest_value:
      largest_key = key
      largest_value = value
  return largest_key

print(max_key({1:100, 2:1, 3:4, 4:10}))

print(max_key({"a":100, "b":10, "c":1000}))