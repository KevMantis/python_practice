# Basta Fazoolin'

# You’ve started position as the lead programmer for the family-style Italian restaurant Basta Fazoolin’ with My Heart. The restaurant has been doing fantastically and seen a lot of growth lately. You’ve been hired to keep things organized.

from datetime import time

# At Basta Fazoolin’ with my Heart our motto is simple: when you’re here with family, that’s great! We have four different menus: brunch, early-bird, dinner, and kids.
# Create a Menu class.
class Menu:
  # Give Menu a constructor with the five parameters self, name, items, start_time, and end_time.
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = time(start_time)
    self.end_time = time(end_time)
  # Give our Menu class a string representation method that will tell you the name of the menu. Also, indicate in this representation when the menu is available.
  def __repr__(self):
    return '{name} available from {start_time} to {end_time}'.format(name = self.name.title(), start_time = self.start_time.strftime('%-I%p'), end_time = self.end_time.strftime('%-I%p'))
  # Give Menu a method .calculate_bill() that has two parameters: self, and purchased_items, a list of the names of purchased items.
  # Have calculate_bill return the total price of a purchase consisiting of all the items in purchased_items.
  def calculate_bill(self, purchased_items):
    total_bill = 0
    for item in purchased_items:
      if item in self.items:
        total_bill += self.items[item]
      else:
        total_bill += 0
    return total_bill

# Let’s create our first menu: brunch. Brunch is served from 11am to 4pm. The following items are sold during brunch:
# {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}
brunch = Menu('brunch menu', {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}, 11, 16)

# Let’s create our second menu item early_bird. Early-bird Dinners are served from 3pm to 6pm. The following items are available during the early-bird menu:
# {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,}
early_bird = Menu('early bird menu', {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,}, 15, 18)

# Let’s create our third menu, dinner. Dinner is served from 5pm to 11pm. The following items are available for dinner:
#{'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,}
dinner = Menu('dinner menu', {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,}, 17, 23)

# And let’s create our last menu, kids. The kids menu is available from 11am until 9pm. The following items are available on the kids menu.
# {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}
kids = Menu('kids menu', {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}, 11, 21)

# Try out our string representation. If you call print(brunch) it should print out something like the following:
# brunch menu available from 11am to 4pm
print(brunch)
print(early_bird)
print(dinner)
print(kids)

# Test out Menu.calculate_bill(). We have a breakfast order for one order of pancakes, one order of home fries, and one coffee. Pass that into brunch.calculate_bill() and print out the price.
print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))

# What about an early-bird purchase? Our last guests ordered the salumeria plate and the vegan mushroom ravioli. Calculate the bill with .caluclate_bill().
print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

# Basta Fazoolin’ with my Heart has seen tremendous success with the family market, which is fantastic because when you’re at Basta Fazoolin’ with my Heart with family, that’s great!
# We’ve decided to create more than one restaurant to offer our fantastic menus, services, and ambience around the country.
# First, let’s create a Franchise class.
class Franchise:
  # Give the Franchise class a constructor. Take in an address, and assign it to self.address. Also take in a list of menus and assign it to self.menus.
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  # Give our Franchises a string represenation so that we’ll be able to tell them apart. If we print out a Franchise it should tell us the address of the restaurant.
  def __repr__(self):
    return self.address
  # Let’s tell our customers what they can order! Give Franchise an .available_menus() method that takes in a time parameter and returns a list of the Menu objects that are available at that time.
  def available_menus(self, time_arg):
    self.time_obj = time(time_arg)
    available = []
    for menu in self.menus:
      if self.time_obj >= menu.start_time and self.time_obj < menu.end_time:
        available.append(menu)
    if len(available) > 0:
      return available
    else:
      return ['None']

# Let’s create our first two franchises! Our flagship store is located at "1232 West End Road" and our new installment is located at "12 East Mulberry Street". Pass in all four menus along with these addresses to define flagship_store and new_installment.
flagship_store = Franchise('1232 West End Road', [brunch, early_bird, dinner, kids])
new_installment = Franchise('12 East Mulberry Street', [brunch, early_bird, dinner, kids])

# Let’s test out our .available_menus() method! Call it with 12 noon as an argument and print out the results.
print(flagship_store.available_menus(12))

# Let’s do another test! If we call .available_menus() with 5pm as an argument and print out the results.
print(flagship_store.available_menus(17))

# My test for no menus available
print(flagship_store.available_menus(10))

# Since we’ve been so successful building out a branded chain of restaurants, we’ve decided to diversify. We’re going to create a restaurant that sells arepas!
# First let’s define a Business class.
class Business:
  # Give Business a constructor. A Business needs a name and a list of franchises.
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises
  # I added this myself
  def __repr__(self):
    if len(self.franchises) > 1:
      return '{name} has {franchises} franchises'.format(name = self.name, franchises = len(self.franchises))
    else:
      return '{name} has {franchises} franchise'.format(name = self.name, franchises = len(self.franchises))
# Let’s create our first Business. The name is "Basta Fazoolin' with my Heart" and the two franchises are flagship_store and new_installment.
business1 = Business('Basta Fazoolin\' with my Heart', [flagship_store, new_installment])

# Print my first business to see its string representation
print(business1)

# Before we create our new business, we’ll need a Franchise and before our Franchise we’ll need a menu. The items for our Take a’ Arepa available from 10am until 8pm are the following:
# {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}
# Save this to a variable called arepas_menu.
arepas_menu = Menu('arepas menu', {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}, 10, 20)

# Next let’s create our first Take a’ Arepa franchise! Our new restaurant is located at "189 Fitzgerald Avenue". Save the Franchise object to a variable called arepas_place.
arepas_place = Franchise('189 Fitzgerald Avenue', [arepas_menu])

# Now let’s make our new Business! The business is called "Take a' Arepa"!
business2 = Business('Take a\' Arepa', [arepas_place])

# Print second business objects
print(arepas_menu)
print(arepas_place)
print(business2)