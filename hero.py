import entity
import random
import map

class Hero(entity.Entity):
  """Extends from entity.
  Attributes: name, max hp, location, row, col"""
  def __init__(self, name, max_hp):
    super().__init__(name, max_hp)
    self.row = 0
    self.col = 0
    self.loc = [self.row, self.col]

  def attack(self, entity):
    """Attacks an enemy, chooses a random damage amount then returns a string of what happened"""
    dmg = random.randint(2,5)
    entity.take_damage(dmg)
    return F"{entity.name} takes a brutal hit from {self.name} for {dmg} damage!"

  """These move the character in the direction the player chooses and ensures that the character never goes out of bounds."""
  def go_north(self):
    if (self.row - 1) < 0:
      return "x"
    else:
      self.row -=1
      self.loc[0] = self.row
      
  def go_south(self):
    m = map.Map()
    if (self.row + 1) >= m.__len__():
      return "x"
    else:
      self.row += 1
      self.loc[0] = self.row

  def go_west(self):
    if (self.col - 1) < 0:
      return "x"
    else:
      self.col -= 1
      self.loc[1] = self.col

  def go_east(self):
    m = map.Map()
    
    if(self.col + 1) >= m.__len__(): #don't use 4, the hardcoded value, change it to rows/cols (variable)
      return "x"
    else:
      self.col += 1
      self.loc[1] = self.col
      return "*"