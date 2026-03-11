

class Player:
    def __init__(self, name, health,inv):
        self.name = name
        self.health = health
        self.inv = inv


class Weapon:
    def __init__(self, name,damage,clip_cap,accuracy,fire_rate):
        self.name = name
        self.damage = damage
        self.clip_cap = clip_cap
        self.accuracy = accuracy
        self.fire_rate = fire_rate

    def shoot(self):
        pass



class Enemy:
    def __init__(self,name,health,weapon):
        self.name = name
        self.health = health
        self.weapon = weapon

    def attack(self):
        pass


class Item:
    def __init__(self,name,value):
        self.name = name
        self.value = value