<<<<<<< HEAD
from hero import Hero


class Dungeon:

    def __init__(self, filename):
        self.list = []
        self.current_x = None
        self.current_y = None
=======
import Hero from hero  #from file import class
import random

class Dungeon:

    def __init__(self, hero):
        self.list=[]
        self.hero=hero
        self.current_x=None
        self.current_y=None

     def map_reading(self, path):
>>>>>>> antoniy
        with open(filename, "r") as in_file:
            lines = in_file.read().splitlines()
            for line in lines:
                self.list.append(line)
    return self.list
             

    def print_map(self):
        for line in self.list:
            print (''.join(line))

    def spawn(self, hero):
        if not (isinstance(hero, Hero)):
            raise Exception("Not A Hero")

        for i in range(0, len(self.list)):
            for j in range(0, len(self.list[i])):
                if self.list[i][j] == "S":
                    self.list[i][j] = "H"
                    self.current_x = i
                    self.current_y = j
<<<<<<< HEAD

    return True
=======
 
    return True

     def pick_the_treasure(self):
        treasures = ["mana", "heal"]
        random_treasure = random.choice(treasures)
        
        if random_treasure == "heal":
            health_points = random.randint(0,100)
            self.hero.take_healing(health_points)
            
        if random_treasure == "mana":
            mana_points = random.randint(0,100)
            self.hero.take_mana(mana_points)
            
    def move_hero(self, direction):
        if direction == "up":
            if self.current_x == 0:
                return False
        new_x = self.current_x - 1
        new_y = self.current_y

        if direction == "down":
            if self.current_x == len(self.list):
                return False

        new_x = self.current_x + 1
        new_y = self.current_y

        if direction == "left":
            if self.current_y == 0:
                return False
        new_y = self.current_y - 1
        new_x = self.current_x

        if direction == "right":
            if self.current_y == len(self.list[0]):
                return False
        new_x = self.current_x
        new_y = self.current_y + 1

        if self.list[new_x][new_y]=="T":
            self.hero.pick_the_treasure

            
>>>>>>> antoniy
