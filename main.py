import hero
import map
import check_input
import expertfactory
import beginnerfactory
import random

def main():
  
  name = input("What is your name traveler?\n")
  map_num = 1
  difficulty = check_input.get_int_range("Select Difficulty:\n1. Beginner\n2. Expert\nChoice: ",1,2)
  
  if difficulty == 1:
    e = beginnerfactory.BeginnerFactory()
  elif difficulty == 2:
    e = expertfactory.ExpertFactory()
  
  h = hero.Hero(name, 25)
  m = map.Map()
  menu = 0
  map_num = 1
  # If the user dies, quits or escapes the game will end
  while (h.hp != 0) and (menu != 5):
    print()
    print(h)
    print()
    print(m.show_map(h.loc))
    menu = check_input.get_int_range("1. Go North\n2. Go South\n3. Go East\n4. Go West\n5. Quit\nEnter Choice: ",1,5)
    if menu == 1:
      flag = h.go_north() 
    elif menu == 2:
     flag = h.go_south()
    elif menu == 3:
     flag = h.go_east()
    elif menu == 4:
     flag = h.go_west()
    else:
      print("You have quit the game.")
      break
    if flag == "x":
      print("--That direction is out of bounds--")
      continue
    else:
      m.reveal(h.loc)
    m.show_map(h.loc)

    # returns the value that the player is on the map
    itemLocation = m[h.loc[0]][h.loc[1]]
    
    if itemLocation == "m":
      enemy = e.create_random_enemy()
      print("You encounter enemy " + enemy.name)
      print("HP: " + str(enemy.hp) + "/" + str(enemy._max_hp) + "\n")
      
      #Prompts the user to attack or run away
      while 1:
        choice = check_input.get_int_range("1. Attack\n2. Run Away\nChoice: ",1,2)

        if choice == 1:
          print(h.attack(enemy))
          if enemy.hp > 0:
            print(enemy.attack(h))
            if h._hp <= 0:
              print("You lose!",enemy.name," has killed you.")
              return 0
          else:
            print(f"You killed {enemy.name}")
            m.remove_at_loc(h.loc)
            break
        elif choice == 2:
          # The hero will run in a random direction
          randomDir = random.randint(1, 4)
          for i in range(1,4):
            if randomDir == i:
              if i == 1:
                if h.loc[1] - 1 < 0:
                  break
                h.go_north()
              elif i == 2:
                if h.loc[1] + 1 > 4:
                  break
                h.go_south()
              elif i == 3:
                h.go_east()
              elif i == 4:
                h.go_west()
          
          m.reveal(h.loc) 
          print("You ran away!")
          break
          
    elif itemLocation == "n":
      print("The room is empty!")
    elif itemLocation == "s":
      print("You are at the start of the dungeon!")
    elif itemLocation == "i":
      print("You found a health potion!")
      print(h.heal())
      m.remove_at_loc(h.loc)
    elif itemLocation == "f":
      print("Congratulations you reached the exit! Onto the next level!")
      map_num += 1
      
      if map_num > 3:
        map_num = 1
      m.load_map(map_num)   
          
main()