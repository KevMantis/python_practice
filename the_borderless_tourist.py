# The Borderless Tourist Project

destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

attractions = []

for index in range(len(destinations)):
  attractions.append([])

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

# Testing work so far
#test_destination_index = get_traveler_location(test_traveler)
#print(test_destination_index)
#print(attractions)

def add_attraction(destination, attraction):
  try:
    destination_index = get_destination_index(destination)
  except ValueError:
    return
  attractions_for_destination = attractions[destination_index]
  attractions_for_destination.append(attraction)
  return

add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

print(attractions)
