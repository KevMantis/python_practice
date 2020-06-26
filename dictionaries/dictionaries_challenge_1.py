# Sum Values

# Write a function named sum_values that takes a dictionary named my_dictionary as a parameter. The function should return the sum of the values of the dictionary
def sum_values(my_dictionary):
  value_sum = 0
  for value in my_dictionary.values():
    value_sum += value
  return value_sum

print(sum_values({"milk":5, "eggs":2, "flour": 3}))

print(sum_values({10:1, 100:2, 1000:3}))