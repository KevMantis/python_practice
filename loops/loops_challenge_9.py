# Same Values

# Write a function named same_values() that takes two lists of numbers of equal size as parameters.

# The function should return a list of the indices where the values were equal in lst1 and lst2.

# For example, the following code should return [0, 2, 3]

# same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5])

def same_values(lst, lst2):
  same_list = []
  for s in range(0, len(lst)):
    l1 = lst[s]
    l2 = lst2[s]
    if l1 == l2:
      same_list.append(s)
  return same_list

print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))
