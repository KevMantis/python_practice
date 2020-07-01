# Attribute Functions

# Instance variables and class variables are both accessed similarly in Python. This is no mistake, they are both considered attributes of an object. If we attempt to access an attribute that is neither a class variable nor an instance variable of the object Python will throw an AttributeError.

# class NoCustomAttributes:
#   pass

# attributeless = NoCustomAttributes()

# try:
#   attributeless.fake_attribute
# except AttributeError:
#   print("This text gets printed!")

# # prints "This text gets printed!"
# What if we aren’t sure if an object has an attribute or not? getattr() is a Python function that works a lot like the usual dot-syntax (i.e., object_name.attribute_name) but we can supply a third argument that will be the default if the object does not have the given attribute. What if we only really care whether the attribute exists? hasattr() will return True if an object has a given attribute and False otherwise.
# Calling those functions looks like this:

# hasattr(attributeless, "fake_attribute")
# # returns False

# getattr(attributeless, "other_fake_attribute", 800)
# # returns 800, the default value
# Above we checked if the attributeless object has the attribute fake_attribute. Since it does not, hasattr() returned False. After that, we used getattr to attempt to retrieve other_fake_attribute. Since other_fake_attribute isn’t a real attribute on attributeless, our call to getattr() returned the supplied default value 800, instead of throwing an AttributeError.

# In script.py we have a list of different data types, some strings, some lists, and some dictionaries, all saved in the variable how_many_s.
# For every element in the list, check if the element has the attribute count. If so, count the number of times the string "s" appears in the element. Print this number.
how_many_s = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for element in how_many_s:
  if hasattr(element, 'count'):
    print(element.count('s'))