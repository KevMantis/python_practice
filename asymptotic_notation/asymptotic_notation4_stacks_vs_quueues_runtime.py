# Stacks vs. Queues Runtime

# In addition to analyzing the runtime of various data structures, it is also important to compare the runtime of different data structures.
# In this exercise, we will compare the runtime of retrieving the first value added to a queue to the runtime of retrieving the first value added to a stack.
# Kirby Zachariah loves to travel! She’s been to six different countries and often forgets the order in which she visited them. However, knowing she has a bad memory, she decided to keep track of the countries she’s visited in both a Queue and a Stack.
# As you can see in the code, the countries have been added both to my_queue and my_stack in the order they were visited.

# 1. Run the code to see what the value at the front of the queue is and what the value at the top of the stack is.

# 2. Change the value of first_value_added_to_queue to the first value added to my_queue. DO NOT simply write "Australia". Use the queue methods to extract the first value. It is ok to remove values from the queue.

# 3. Given that N is the size of the initial queue, change the value of queue_runtime to the big O runtime of getting the first value added to the queue. Select from the the following options:
# - "1"
# - "N"
# - "log N"
# - "N log N"
# - "N^2"
# - "2^N"
# - "N!"

# 4. Change the value of first_value_added_to_stack to the first value pushed onto my_stack. DO NOT simply write "Australia". Use the stack methods to extract the first value. It is ok to remove values from the stack. Check the hint if you want to see how to retrieve the first value added to the stack.

# 5. Given that N is the size of the initial stack, change the value of stack_runtime to the big O runtime of getting the first value pushed onto the stack. Select from the following options:
# - "1"
# - "N"
# - log N"
# - N log N"
# - N^2"
# - "2^N"
# - N!"

from stack import Stack
from queue import Queue

N = 6

my_stack = Stack(N)
my_stack.push("Australia")
my_stack.push("India")
my_stack.push("Costa Rica")
my_stack.push("Peru")
my_stack.push("Ghana")
my_stack.push("Indonesia")

my_queue = Queue(N)
my_queue.enqueue("Australia")
my_queue.enqueue("India")
my_queue.enqueue("Costa Rica")
my_queue.enqueue("Peru")
my_queue.enqueue("Ghana")
my_queue.enqueue("Indonesia")

#Print the first values in the stack and queue
print("The top value in my stack is: {0}".format(my_stack.peek()))
print("The front value of my queue is: {0}".format(my_queue.peek()))

#Get First Value added to Queue
first_value_added_to_queue = my_queue.peek() #Checkpoint 2
print("\nThe first value enqueued to the queue was {0}".format(first_value_added_to_queue))
queue_runtime = "1" #Checkpoint 3
print("The runtime of getting the front of the queue is O({0})".format(queue_runtime))

#Get First Value added to Stack
#Write Code Here for #Checkpoint 4
first_value_added_to_stack = [my_stack.pop() for each in range(my_stack.size)][-1]
print("\nThe first value pushed onto the stack was {0}".format(first_value_added_to_stack))
stack_runtime = "N" #Checkpoint 5
print("The runtime of getting the bottom of the stack is O({0})".format(stack_runtime))