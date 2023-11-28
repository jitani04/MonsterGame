import enemyfactory
import random
import easytroll
import easygoblin
import easyogre

class BeginnerFactory(enemyfactory.EnemyFactory):
  """factory to create easy enemies"""
  
  def create_random_enemy(self):
     """randomizes and constructs one of the easy enemies"""
     e_choice = random.randint(1,3)
     if e_choice == 1:
       return easytroll.EasyTroll()
     elif e_choice == 2:
       return easyogre.EasyOgre()
     else:
       return easygoblin.EasyGoblin()
     