import entity
import random
class EasyGoblin(entity.Entity):
  def __init__(self):
    """randomize hp to 3-4, call super for name and hp"""
    hp = random.randint(3, 4) # Need to figure out how to change in the random hp value
    super().__init__("Gogo", hp)

  def attack(self, entity):
    """enemy attacks hero, randomize damage and give it to hero, then return a string representing the attack"""
    
    dmg = random.randint(1,3)
    entity.take_damage(dmg)
    return self.name + " attacks " + entity.name + " for " + str(dmg) + " damage."
    