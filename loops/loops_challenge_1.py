# Divisible by Ten

# Create a function named divisible_by_ten() that takes a list of numbers named nums as a parameter.

# Return the count of how many numbers in the list are divisible by 10.

def divisible_by_ten(nums):
  div_by_10_list = []
  for num in nums:
    if num % 10 == 0:
      div_by_10_list.append(num)
  return len(div_by_10_list)

print(divisible_by_ten([20, 25, 30, 35, 40])) # Should return 3
