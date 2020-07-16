class Pokemon:
  def __init__(self, name, type, level=5):
    self.name = name
    self.type = type
    self.level = level
    self.max_health = level * 5
    self.health = self.max_health
    self.knocked_out = False

  def __repr__(self):
    return 'This level {level} {name} {type} type Pokemon has {health} hit points remaining.'.format(level = self.level, name = self.name, type = self.type, health=self.health)

  def revive(self):
    self.knocked_out = False
    if self.health == 0:
      self.health = 1
    print('{name} was revived!'.format(name = self.name))

  def knock_out(self):
    self.knocked_out = True
    if self.health != 0:
      self.health = 0
    print('{name} was knocked out!'.format(name = self.name))

  def lose_health(self, amount):
    self.health -= amount
    if self.health <= 0:
      self.health = 0
      self.knock_out()
    else:
      print('{name} now has {health} health.'.format(name = self.name, health = self.health))

  def gain_health(self, amount):
    if self.health == 0:
      self.revive()
    self.health += amount
    if self.health >= self.max_health:
      self.health = self.max_health
    print('{name} now has {health} health.'.format(name = self.name, health = self.health))

  def attack(self, other_pokemon):
    if self.knocked_out:
      print('{name} can\'t attack because it is knocked out!'.format(name = self.name))
      return
    if (self.type == 'Fire' and other_pokemon.type == 'Water') or (self.type == 'Fire' and other_pokemon.type == 'Fire') or (self.type == 'Water' and other_pokemon.type == 'Grass') or (self.type == 'Water' and other_pokemon.type == 'Water') or (self.type == 'Grass' and other_pokemon.type == 'Fire') or (self.type == 'Grass' and other_pokemon.type == 'Grass') or (self.type == 'Electric' and other_pokemon.type == 'Grass'):
      print('{my_name} attacked {other_name} for {damage} damage.'.format(my_name = self.name, other_name = other_pokemon.name, damage = round(self.level * 0.5)))
      print('It\'s not very effective!')
      other_pokemon.lose_health(round(self.level * 0.5))
    if (self.type == 'Fire' and other_pokemon.type == 'Electric') or (self.type == 'Water' and other_pokemon.type == 'Electric') or (self.type == 'Grass' and other_pokemon.type == 'Electric'):
      print('{my_name} attacked {other_name} for {damage} damage.'.format(my_name = self.name, other_name = other_pokemon.name, damage = self.level))
      other_pokemon.lose_health(self.level)
    if (self.type == 'Fire' and other_pokemon.type == 'Grass') or (self.type == 'Water' and other_pokemon.type == 'Fire') or (self.type == 'Grass' and other_pokemon.type == 'Water') or (self.type == 'Electric' and other_pokemon.type == 'Water'):
      print('{my_name} attacked {other_name} for {damage} damage.'.format(my_name = self.name, other_name = other_pokemon.name, damage = self.level * 2))
      print('It\'s super effective!')
      other_pokemon.lose_health(self.level * 2)

class Charmander(Pokemon):
  def __init__(self, level = 5):
    super().__init__('Charmander', 'Fire', level)

class Squirtle(Pokemon):
  def __init__(self, level = 5):
    super().__init__('Squirtle', 'Water', level)

class Bulbasaur(Pokemon):
  def __init__(self, level = 5):
    super().__init__('Bulbasaur', 'Grass', level)

class Pikachu(Pokemon):
  def __init__(self, level = 5):
    super().__init__('Pikachu', 'Electric', level)

class Trainer:
  def __init__(self, pokemon_list, potions, name):
    self.pokemon_list = pokemon_list
    self.potions = potions
    self.current_pokemon = 0
    self.name = name

  def __repr__(self):
    print('The trainer {name} has the following pokemon'.format(name = self.name))
    for pokemon in self.pokemon_list:
        print(pokemon)
    return 'The current active pokemon is {name}'.format(name = self.pokemon_list[self.current_pokemon].name)

  def switch_active_pokemon(self, new_active):
    if new_active < len(self.pokemon_list) and new_active >= 0:
      if self.pokemon_list[new_active].knocked_out:
        print('{name} is knocked out. You can\'t make it your active pokemon'.format(name = self.pokemon_list[new_active].name))
      elif new_active == self.current_pokemon:
        print('{name} is already your active pokemon'.format(name = self.pokemon_list[new_active].name))
      else:
        self.current_pokemon = new_active
        print('Go {name}, it\'s your turn!'.format(name = self.pokemon_list[self.current_pokemon].name))

  def use_potion(self):
    if self.potions > 0:
      print('You used a potion on {name}.'.format(name = self.pokemon_list[self.current_pokemon].name))
      self.pokemon_list[self.current_pokemon].gain_health(20)
      self.potions -= 1
    else:
      print('You don\'t have any more potions')

  def attack_other_trainer(self, other_trainer):
    my_pokemon = self.pokemon_list[self.current_pokemon]
    their_pokemon = other_trainer.pokemon_list[other_trainer.current_pokemon]
    my_pokemon.attack(their_pokemon)

pokemon_1 = Charmander(7)
pokemon_2 = Squirtle()
pokemon_3 = Pikachu(1)
pokemon_4 = Bulbasaur(10)
pokemon_5 = Charmander()
pokemon_6 = Squirtle(2)

lucas = Trainer([pokemon_1,pokemon_2,pokemon_3], 3, 'Lucas')
dawn = Trainer([pokemon_4,pokemon_5,pokemon_6], 5, 'Dawn')

print(lucas)
print(dawn)

lucas.attack_other_trainer(dawn)
dawn.attack_other_trainer(lucas)
dawn.use_potion()
lucas.attack_other_trainer(dawn)
dawn.switch_active_pokemon(0)
dawn.switch_active_pokemon(1)