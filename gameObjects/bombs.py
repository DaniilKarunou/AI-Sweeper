import random
from abc import ABC as abstract, abstractmethod
from random import randint

class Bomb(abstract):

    @abstractmethod
    def __init__(self):
        self.id = int()
        self.weight = int()
        self.time = str()
        self.explosion_radius = str()
        self.place_ground = str()
        self.visibility = str()
        self.old_or_not = str()
        self.location = []

    @abstractmethod
    def type(self):
        pass

    def get_info(self):
        info = {    'type of bomb': self.type(),
                    'time': self.time,
                    'explosion_radius': self.explosion_radius,
                    'place_ground': self.place_ground,
                    'visibility': self.visibility,
                    'old_or_not': self.old_or_not,
        }
        return info

class Mine(Bomb):

#42 - ok
    def __init__(self, location):
        self.id = 0
        self.weight = 2
        self.time = "a lot of time"
        self.explosion_radius = "none"
        self.place_ground = str(str(random.choice(["grass"])))
        self.visibility = str(random.choice(["50-60", "60-70", "70-80", "80-90", "90-100"]))
        self.old_or_not = randint(0, 1)
        self.location = location

    def type(self):
        return "Mine"


class Grenade(Bomb):

#192 - ok
    def __init__(self, location):
        self.id = 1
        self.weight = 1
        self.time = str(random.choice(["a lot of time", "a little time", "a few seconds"]))
        self.explosion_radius = "none"
        self.place_ground = str(str(random.choice(["rock"])))
        self.visibility = str(random.choice(["60-70", "70-80", "80-90", "90-100"]))
        self.old_or_not = randint(0, 1)
        self.location = location

    def type(self):
        return "Grenade"

class WaterMine(Bomb):

#48-ok
    def __init__(self, location):
        self.id = 2
        self.weight = 3
        self.time = "a lot of time"
        self.explosion_radius = "medium"
        self.place_ground = str(str(random.choice(["water"])))
        self.visibility = str(random.choice(["40-50", "50-60", "60-70", "70-80", "80-90", "90-100"]))
        self.old_or_not = randint(0, 1)
        self.location = location

    def type(self):
        return "WaterMine"

class AirBomb(Bomb):

#24-ok
    def __init__(self, location):
        self.id = 3
        self.weight = 2
        self.time = str(random.choice(["a lot of time", "a little time", "a few seconds"]))
        self.explosion_radius = "medium"
        self.place_ground = str(str(random.choice(["grass"])))
        self.visibility = "90-100"
        self.old_or_not = randint(0, 1)
        self.location = location

    def type(self):
        return "AirBomb"

class C4(Bomb):

#72-ok
    def __init__(self, location):
        self.id = 4
        self.weight = 2
        self.time = str(random.choice(["a lot of time", "a little time", "a few seconds"]))
        self.explosion_radius = "none"
        self.place_ground = str(str(random.choice(["grass"])))
        self.visibility = str(random.choice(["70-80", "80-90", "90-100"]))
        self.old_or_not = randint(0, 1)
        self.location = location

    def type(self):
        return "C4"

class FakeBomb(Bomb):

#96-ok
    def __init__(self, location):
        self.id = 5
        self.weight = 1
        self.time = str(random.choice(["a lot of time", "a little time", "a few seconds"]))
        self.explosion_radius = "none"
        self.place_ground = str(str(random.choice(["grass"])))
        self.visibility = str(random.choice(["60-70", "70-80", "80-90", "90-100"]))
        self.old_or_not = randint(0, 1)
        self.location = location

    def type(self):
        return "FakeBomb"

class HandBomb(Bomb):

#48-ok
    def __init__(self, location):
        self.id = 6
        self.weight = 1
        self.time = str(random.choice(["a little time", "a few seconds"]))
        self.explosion_radius = "none"
        self.place_ground = str(str(random.choice(["grass"])))
        self.visibility = str(random.choice(["70-80", "80-90", "90-100"]))
        self.old_or_not = randint(0, 1)
        self.location = location

    def type(self):
        return "HandBomb"

class Molotov(Bomb):

#48-ok
    def __init__(self, location):
        self.id = 7
        self.weight = 1
        self.time = str(random.choice(["a little time", "a few seconds"]))
        self.explosion_radius = "none"
        self.place_ground = str(str(random.choice(["grass"])))
        self.visibility = str(random.choice(["70-80", "80-90", "90-100"]))
        self.old_or_not = randint(0, 1)
        self.location = location

    def type(self):
        return "Molotov"

class NukeBomb(Bomb):

#24-ok
    def __init__(self, location):
        self.id = 8
        self.weight = 3
        self.time = str(random.choice(["a lot of time", "a little time", "a few seconds"]))
        #self.explosion_type = "drop"
        self.explosion_radius = "huge"
        self.place_ground = str(str(random.choice(["grass"])))
        self.visibility = "90-100"
        self.old_or_not = randint(0, 1)
        self.location = location

    def type(self):
        return "NukeBomb"

class TNT(Bomb):

#48-ok
    def __init__(self, location):
        self.id = 9
        self.weight = 3
        self.time = str(random.choice(["a lot of time", "a few seconds"]))
        #self.explosion_type = "timer"
        self.explosion_radius = "none"
        self.place_ground = str(str(random.choice(["grass"])))
        self.visibility = str(random.choice(["70-80", "80-90", "90-100"]))
        self.old_or_not = randint(0, 1)
        self.location = location

    def type(self):
        return "TNT"