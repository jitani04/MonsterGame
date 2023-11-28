import troll
import goblin
import ogre
import enemyfactory
import random

class ExpertFactory(enemyfactory.EnemyFactory):
  """factory to create more difficult enemies"""
  
  def create_random_enemy(self):
     """randomizes and creates one of the difficult enemies (Troll, Ogre, or Goblin)"""
     e_choice = random.randint(1,3)
     if e_choice == 1:
       return troll.EvilTroll()
     elif e_choice == 2:
       return ogre.ViolentOgre()
     else:
       return goblin.DeadlyGoblin()
    