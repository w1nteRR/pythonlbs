# pylint: disable-msg=E0611
from objects.Object import *
from enums.Season import *
from enums.SportType import *

class SkiJumpingCenter(Object):
    sport_type = SportType.SKIHUMPING
    season = Season.WINTER

    def __init__(self, length, name, capacity, location):
         self.length = length
         self.name = name
         self.capacity = capacity
         self.location = location

    def __str__(self):
        return "Type: " + str(self.sport_type.value) + " Capacity: " + str(self.capacity) + " Location: " + str(self.location) 
