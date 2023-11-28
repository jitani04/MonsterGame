import entity
import random

class DeadlyGoblin(entity.Entity):
  """randomize the hp to 6-10, calls the super for the name and hp"""
  def __init__(self):
    hp = random.randint(6,10)
    super().__init__("Deadly Gogo", hp)

  def attack(self, entity):
    """enemy attacks hero, randomize damage and give it to hero, then return a string representing the attack"""
    
    dmg = random.randint(4,8)
    entity.take_damage(dmg)
    return self.name + " attacks " + entity.name + " for " + str(dmg) + " damage."
    
    