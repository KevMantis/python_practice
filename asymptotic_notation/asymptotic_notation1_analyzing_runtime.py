# Analyzing Runtime

# Now that you’ve started learning how to use asymptotic notation to measure the runtime of a function, let’s practice with Python!
# When analyzing the runtime of a function, it’s necessary to check the number of iterations the loop will perform based on the size of the input.
# The count function on the left takes in a positive integer of size N and returns the number of times it takes to divide N by 2 until N reaches 1.
# We can analyze the runtime of this function by counting the number of iterations the while loop will perform based on the size of the input.

# Change the values of num_iterations_1, num_iterations_2, num_iterations_4, num_iterations_32, and num_iterations_64 to the number of iterations the while loop will perform when N is respectively 1, 2, 4, 32, and 64.

def count(N):
  count = 0
  while N > 1:
    N = N//2
    count += 1
  return count


num_iterations_1 = 0 #REPLACE
print("The while loop performs {0} iterations when N is 1".format(num_iterations_1))

num_iterations_2 = 1 #REPLACE
print("\nThe while loop performs {0} iterations when N is 2".format(num_iterations_2))

num_iterations_4 = 2 #REPLACE
print("\nThe while loop performs {0} iterations when N is 4".format(num_iterations_4))

num_iterations_32 = 5 #REPLACE
print("\nThe while loop performs {0} iterations when N is 32".format(num_iterations_32))

num_iterations_64 = 6 #REPLACE
print("\nThe while loop performs {0} iterations when N is 64".format(num_iterations_64))

# Do you notice a pattern forming? With N being divided by 2 each iteration, we can use that to establish a big O runtime.
# Change the value of runtime to whichever one of these values you think the big O runtime is:
# - "1"
# - "N"
# - "log N"
# - "N log N"
# - "N^2"
# - "2^N"
# - "N!"

runtime = "log N"
print("\nThe runtime for this function is O({0})".format(runtime))

print(count(64))
