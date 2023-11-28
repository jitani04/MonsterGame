import abc

class Entity(abc.ABC):
  """describes a character in the game"""
  
  def __init__(self, name, max_hp):
    """ Initializes each of the instance variables: name, hp , max hp."""
    self._name = name
    self._hp = max_hp
    self._max_hp = max_hp

  @property
  def name(self):
    return self._name

  @property
  def hp(self):
    return self._hp

  def take_damage(self, dmg):
    """Allows one entity to damage another"""
    if (self._hp - dmg) < 0:
      self._hp = 0
    else:
      self._hp -= dmg

  def heal(self):
    """Heals the entity to full hp"""
    self._hp = self._max_hp
    return "HP restored to FULL!"

  def __str__(self):
    return "Name: {}\nHP: {}/{}".format(self._name, self._hp, self._max_hp)

  @abc.abstractmethod
  def attack(self, entity):
    pass


    