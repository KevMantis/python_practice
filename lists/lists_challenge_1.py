# 1. Append Sum

# Write a function named append_sum that has one parameter — a list named named lst.

# The function should add the last two elements of lst together and append the result to lst. It should do this process three times and then return lst.

For example, if lst started as [1, 1, 2], the final result should be [1, 1, 2, 3, 5, 8].

def append_sum(lst):
  l = 0
  while l < 3:
    last_two_sum = lst[-1] + lst[-2]
    lst.append(last_two_sum)
    l += 1
  return lst
print(append_sum([1, 1, 2]))
