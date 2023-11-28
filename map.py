
class Map:
  """The map is used by the hero, whenever the hero moves the map will be updated. """
  _instance = None
  _initialized = False

  def __new__(cls, *args):
      if cls._instance is None:
          cls._instance = super().__new__(cls)
      return cls._instance

  def __init__(self):
    if not Map._initialized:
      self.load_map(1)
      Map._initialized = True
      
          
  def __getitem__(self, row):
    """returns the specified row from the map, overloaded [] operator"""
    return self._map[row]
    
  def __len__(self):
    """returns the number of rows in the map list"""
    return len(self._map) # Should equal 5

  def show_map(self, loc):
    """Returns the map in string format (5x5 matrix) of  characters, another 5x5 matrix is created and initialized with false values. """
    tempStr = ""
    for i in range(0, self.__len__()):
      for j in range(0, self.__len__()):
        # Check if players loc(row, col) = i, j then put player "*" in that position
        if (i == loc[0]) and (j == loc[1]):  
          self.reveal(loc)
          tempStr += "* "
        elif self._revealedList[i][j] == False:
          tempStr += "x "
        else: 
          tempStr = tempStr + str(self._map[i][j]) + " "
        
      tempStr += "\n"
    return tempStr

  def reveal(self, loc):
    """Reveals the location that the player stepped over."""
    self._revealedList[loc[0]][loc[1]] = True

  def remove_at_loc(self, loc):
    """Primarily used after a monster is killed or item is picked up. The position value is changed to N after the action has been done."""
    self._map[loc[0]][loc[1]] = "n"

  def load_map(self, map_num):
    map_list = ["map1.txt", "map2.txt", "map3.txt"]
    if map_num == 1:
      self._file = open(map_list[0])
    elif map_num == 2:
      self._file = open(map_list[1])
    elif map_num == 3:
      self._file = open(map_list[2])
    # Create 2D map and initialize values from map.txt into _map.
    # Create and fill the 2D revealed list with all False values.
    self._map = []
    self._revealedList = []
    for line in self._file:
      list = []
      rList = []
      for char in line:
        list.append(char)
        rList.append(False)
      self._map.append(list)
      self._revealedList.append(rList)
  