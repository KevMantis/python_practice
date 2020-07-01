# Review

# So far we’ve covered what a data type actually is in Python. We explored what the functionality of Python’s built-in types (also referred to as primitives) are. We learned how to create our own data types using the class keyword.
# We explored the relationship between a class and an object — we create objects when we instantiate a class, we find the class when we check the type() of an object. We learned the difference between class variables (the same for all objects of a class) and instance variables (unique for each object).
# We learned about how to define an object’s functionality with methods. We created multiple objects from the same class, all with similar functionality, but with different internal data. They all had the same methods, but produced different output because they were different instances.
# Take a moment to congratulate yourself, object-oriented programming is a complicated concept.

# Define a class Student this will be our data model at Jan van Eyck High School and Conservatory.
class Student:
  # Add a constructor for Student. Have the constructor take in two parameters: a name and a year. Save those two as attributes .name and .year.
  def __init__(self, name, year):
    self.name = name
    self.year = year
    # In the body of the constructor for Student, declare self.grades as an empty list.
    self.grades = []

  # Add an .add_grade() method to Student that takes a parameter, grade.
  # .add_grade() should verify that grade is of type Grade and if so, add it to the Student‘s .grades.
  # If grade isn’t an instance of Grade then .add_grade() should do nothing.
  def add_grade(self, grade):
    if type(grade) == Grade:
      self.grades.append(grade)
    else:
      pass

#Create three instances of the Student class:
# Roger van der Weyden, year 10
# Sandro Botticelli, year 12
# Pieter Bruegel the Elder, year 8
# Save them into the variables roger, sandro, and pieter.
roger = Student('Roger van der Weyden', 10)
sandro = Student('Sandro Botticelli', 12)
pieter = Student('Pieter Bruegel the Elder', 8)

# Create a Grade class, with minimum_passing as an attribute set to 65.
class Grade:
  minimum_passing = 65
  # Give Grade a constructor. Take in a parameter score and assign it to self.score.
  def __init__(self, score):
    self.score = score

# Create a new Grade with a score of 100 and add it to pieter‘s .grades attribute using .add_grade().
pieter.add_grade(Grade(100))

#Great job! You’ve created two classes and defined their interactions. This is object-oriented programming! From here you could:
# -Write a Grade method .is_passing() that returns whether a Grade has a passing .score.
# -Write a Student method get_average() that returns the student’s average score.
# -Add an instance variable to Student that is a dictionary called .attendance, with dates as keys and booleans as values that indicate whether the student attended school that day.
# -Write your own classes to do whatever logic you want!