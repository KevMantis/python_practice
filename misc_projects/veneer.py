# Veneer

# Here at Veneer we strive to provide the best marketplace experience to connect vetted art dealers with premium galleries. Create a marketplace for people and organizations to buy and sell pieces of art!
# In this project we’ll be developing classes and objects that represent the various responsibilities of art dealership software.

# Here at Veneer, our main concern is the buying and selling of priceless art works. Let’s start out by building a model for these works of art.
# Define a class called Art.

class Art:
  # Give Art a constructor that takes self and four additional parameters: artist, title, medium, and year.
  # Assign these values to self.artist, self.title, self.medium and self.year.
  def __init__(self, artist, title, medium, year, owner):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    # Now that we have Clients our works of Art can have owners! Let’s update our Art class constructor to take an additional parameter, owner, and assign that to self.owner.
    self.owner = owner
  # Give your Art class a string representation method. This method should return a representation of the artwork in as close to standard citation format as we can manage (without italics). It should state:
  # -The artist’s name
  # -The name of the artwork in quotes
  # -The year the work was created
  # -The medium
  # For instance:
  # Monet, Claude. "Vétheuil in the Fog". 1879, oil on canvas.
  def __repr__(self):
    # A full citation of a work of art necessarily includes the name of the person/entity whose collection it includes, as well as the location if that place is a museum.
    # Because the work of art has an owner property, we can retrieve some of that information from self.owner.
    # Let’s update Art‘s string representation method to add the self.owner.name at the very end, followed by a comma, followed by self.owner.location, followed by a period.
    return '{}. {}. {}, {}. {}, {}.'.format(self.artist, self.title, self.year, self.medium, self.owner.name, self.owner.location)

# Let’s see how our Art class looks, create a new work of art. Our first client wants to list a particular Picasso painting to make more space for her new fascination with Italian Futurism, so let’s see if we can use our data model for this piece:
# The artist is “Picasso, Pablo”.
# The work’s title is “Girl with a Mandolin (Fanny Tellier)”.
# The artwork was created in 1910.
# The medium is “oil on canvas”.
# Save this work of art into the variable girl_with_mandolin.
##girl_with_mandolin = Art('Picasso, Pablo', '“Girl with a Mandolin (Fanny Tellier)”', 'oil on canvas', 1910, edytta)
# Print out girl_with_mandolin and run your code, does your code produce this output?
# Picasso, Pablo. "Girl with a Mandolin (Fanny Tellier)". 1910, oil on canvas.
##print(girl_with_mandolin)

# In order to buy and sell works of art, we need a marketplace that will maintain the responsibilities of buying, selling, listing, and delisting of those artworks.
# Create a new class called Marketplace.
class Marketplace:
  # Give your Marketplace class a constructor. In Marketplace‘s constructor, define self.listings as a new list.
  def __init__(self):
    self.listings = []
  # Create an .add_listing() method for your Marketplace class. This should take two arguments: self and new_listing. Have .add_listing() add the new listing to Marketplace‘s listings attribute.
  def add_listing(self, new_listing):
    self.listings.append(new_listing)
  # Since we’ll need a way to remove listings when they expire or are acted upon, let’s implement a .remove_listing() method for our Marketplace
  def remove_listing(self, listing):
    self.listings.remove(listing)
  # The main usage of our application will be the perusal of a marketplace’s listings. Let’s include that functionality as well.
  # Add a .show_listings() method to your Marketplace class that iterates through each listing in self.listings and prints them all out.
  def show_listings(self):
    for listing in self.listings:
      print(listing)

# Create our main marketplace by instantiating Marketplace and saving it into the variable veneer.
veneer = Marketplace()

# Print out the results of veneer.show_listings(). This should be empty for now so won’t print anything, but it’s good to test if your code has any errors!
veneer.show_listings()

# Now for the most important aspect of a marketplace, clients! Create a new class called Client.
class Client:
  # Give our Client class a constructor. A client should have the following data:
  # self.name the name of the person or institution.
  # self.location is the name of the location of the museum or “Private Collection” if the client is a collector.
  # self.is_museum, a boolean value representing whether the client is a museum (if True) or a collector (if False).
  # name, location, and is_museum should all be passed as arguments to the constructor.
  def __init__(self, name, is_museum=False, location='Private Collection'):
    self.name = name
    self.is_museum = is_museum
    self.location = location
  # Update our Client class to have a new method, .sell_artwork(). This method should take three parameters: self, artwork, and price.
  # .sell_artwork() should do the following:
  # Check that artwork.owner is the same (==) as self (i.e., make sure the client owns the art they’re trying to sell).
  # Create a new Listing with the given art, price, and client.
  # Add the listing to the marketplace using veneer.add_listing().
  def sell_artwork(self, artwork, price):
    if artwork.owner == self:
      new_listing = Listing(artwork, price, self)
      veneer.add_listing(new_listing)
  # There’s one last piece of functionality before we’re ready to hit the market (so to speak), our clients need to be able to buy art!
  # Create a .buy_artwork() method for the Client class. .buy_artwork() should take two arguments: self and artwork.
  # Start by having .buy_artwork() check that the artwork is not owned by the client.
  def buy_artwork(self, artwork):
    if artwork.owner != self:
    # The next thing .buy_artwork() should do is make sure that the artwork is listed in veneer.listings. Save the appropriate listing as art_listing, we’ll need to remove it later.
      art_listing = None
      for listing in veneer.listings:
        if listing.art == artwork:
          art_listing = listing
          break
    # If the art is not currently owned and is listed then go through with the transaction! .buy_artwork() should do the following:
    # Change the artwork.owner to the client doing the purchasing.
    # Remove the listing from the marketplace using veneer.remove_listing()
    if art_listing is not None:
      artwork.owner = self
      veneer.remove_listing(art_listing)

# Now instantiate our first Client: her name is Edytta Halpirt and she is a collector and not a museum.
# Save our new Client to a variable called edytta.
edytta = Client('Edytta Halpirt')
# Every purchase requires a buyer and a seller, let’s create a second Client with the following information:
# It’s name is “The MOMA”
# It is located in “New York”
# It is a museum.
# Save this Client to a variable called moma.
moma = Client('The MOMA', True, 'New York')

# We need to get the MOMA to purchase a Picasso from Edytta, but for now try running your code to make sure our Client class doesn’t produce any errors.

# Move our instantiation of girl_with_mandolin to after our instantiation of edytta. When creating the Art object for girl_with_mandolin, pass in edytta as the owner.
girl_with_mandolin = Art('Picasso, Pablo', '“Girl with a Mandolin (Fanny Tellier)”', 'oil on canvas', 1910, edytta)

# Move our print statement printing out girl_with_mandolin to after its new instantiation. Does it print out the following?
# Picasso, Pablo. "Girl with a Mandolin (Fanny Tellier)". 1910, oil on canvas. Edytta Halpirt, Private Collection.
print(girl_with_mandolin)

# Now that we have a marketplace to facilitate the buying and selling, let’s create our class to list works of art!
# Create a new class called Listing. We’ll use these as listings for our Marketplace.
class Listing:
  # Our Listing class needs a constructor! It should define the following instance variables:
  # self.art, the work of art being listed
  # self.price, the price of the work
  # self.seller an instance of Client.
  # Each instance variable should be set equal to an argument passed to the constructor.
  def __init__(self, art, price, seller):
    # Our Listing class needs a constructor! It should define the following instance variables:
    # self.art, the work of art being listed
    # self.price, the price of the work
    # self.seller an instance of Client.
    # Each instance variable should be set equal to an argument passed to the constructor.
    self.art = art
    self.price = price
    self.seller = seller
  # Give the Listing a string representation which should print out the following:
  # The name of the work of art
  # The price of the work of art
  # Remember not to use the string representation of Art for this, it’s too verbose and our clientele will want to parse the listings without reading all of the metadata unless they’re interested in purchasing in the artwork.
  def __repr__(self):
    return '{}, {}.'.format(self.art.title, self.price)

# Use edytta.sell_artwork() to create a listing for girl_with_mandolin. Edytta wants to sell it for $6M (USD).
edytta.sell_artwork(girl_with_mandolin, '$6M (USD)')

# Call veneer.show_listings(), is our newly listed work of art on the market?
veneer.show_listings()

# The MOMA is very interested in purchasing girl_with_mandolin. Call .buy_artwork() from the moma instance with girl_with_mandolin as an argument.
moma.buy_artwork(girl_with_mandolin)

# Finally, print out girl_with_mandolin one last time. It should display the following:
# Monet, Claude. "Vétheuil in the Fog". 1879, oil on canvas. The MOMA, New York.
print(girl_with_mandolin)

# Also call veneer.show_listings(). There shouldn’t be any listings left! Congrats on one purchase successfully made!
veneer.show_listings()