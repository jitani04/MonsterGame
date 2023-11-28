import entity
import random

class ViolentOgre(entity.Entity):
  """randomize the hp to 8-12, calls the super for the name and hp"""
  def __init__(self):
    hp = random.randint(8,12)
    super().__init__("Violent Shrek", hp)

  def attack(self, entity):
    """enemy attacks hero, randomize damage and give it to hero, then return a string representing the attack"""
    
    dmg = random.randint(6,10)
    entity.take_damage(dmg)
    return self.name + " attacks " + entity.name + " for " + str(dmg) + " damage."