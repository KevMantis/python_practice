# The Borderless Tourist Project

destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

# My first attempt at this function until I read the hint and learned about the List .index() method
#def get_destination_index(destination):
#  for index in range(len(destinations)):
#    if destination == destinations[index]:
#      destination_index = index
#  return destination_index

def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

# Testing work so far
#print(get_destination_index("Los Angeles, USA"))
#print(get_destination_index("Paris, France"))
#print(get_destination_index("Hyderabad, India"))

# Interim version of the function while stepping through instructions
#def get_traveler_location(traveler):
#  traveler_destination = traveler[1]
#  return traveler_destination

# Testing work so far
#print(get_traveler_location(test_traveler))
#traveler_destination_index = get_destination_index(get_traveler_location(test_traveler))
#print(traveler_destination_index)

# Final version of the function
def get_traveler_location(traveler):
  traveler_destination_index = get_destination_index(traveler[1])
  return traveler_destination_index

test_destination_index = get_traveler_location(test_traveler)
print(test_destination_index)
