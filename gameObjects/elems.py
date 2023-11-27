from abc import ABC as abstract, abstractmethod

class Elementy(abstract):

    @abstractmethod
    def __init__(self):
        self.koszt = int()

    @abstractmethod
    def elementy_type(self):
        pass

class Grass(Elementy):

    def __init__(self):
        self.koszt = 1

    def elementy_type(self):
        return "grass"

class Rock(Elementy):

    def __init__(self):
        self.koszt = 2

    def elementy_type(self):
        return "rock"

class Duzykamien(Elementy):

    def __init__(self):
        self.koszt = 5

    def elementy_type(self):
        return "duzykamien"

class Kaluza(Elementy):

    def __init__(self):
        self.koszt = 4

    def elementy_type(self):
        return "kaluza"