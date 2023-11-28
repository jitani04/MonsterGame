import entity
import random

class EvilTroll(entity.Entity):
  """randomize the hp to 10-14, calls the super for the name and hp
"""
  def __init__(self):
    hp = random.randint(10,14)
    super().__init__("Evil Poppy", hp)

  def attack(self, entity):
    """enemy attacks hero, randomize damage and give it to hero, then return a string representing the attack"""
    
    dmg = random.randint(8,12)
    entity.take_damage(dmg)
    return self.name + " attacks " + entity.name + " for " + str(dmg) + " damage."