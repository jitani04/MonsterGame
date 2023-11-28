import entity
import random

class EasyOgre(entity.Entity):
  def __init__(self):
    """randomize hp to 3-5, call super for name and hp"""
    hp = random.randint(3, 5) # Need to figure out how to change in the random hp value
    super().__init__("Shrek", hp)

  def attack(self, entity):
    """enemy attacks hero, randomize damage and give it to hero, then return a string representing the attack"""
    
    dmg = random.randint(1,4)
    entity.take_damage(dmg)
    return self.name + " attacks " + entity.name + " for " + str(dmg) + " damage."
    