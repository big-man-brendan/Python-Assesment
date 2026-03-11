import time

class Player:
    def __init__(self, name, health,inv):
        self.name = name
        self.health = health
        self.inv = inv


class Weapon:
    def __init__(self, name,damage,clip_cap,accuracy,fire_rate,bullet,value,pickup_message):
        self.name = name
        self.damage = damage
        self.clip_cap = clip_cap
        self.accuracy = accuracy
        self.fire_rate = fire_rate
        self.bullet = bullet
        self.value = value
        self.pickup_message = pickup_message

    def shoot(self):
        pass

    def pick_up(self):
        print(self.pickup_message)


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



def slow_text(text):

    for i in text:
        print(text[i])
        time.sleep(0.03)



weapons = []

weapon_data = [
    ("AK-47",40,30,70,650,"assault",500,"You pick up the AK-47, Chambered in 7.62. It feels heavy in your hands. Maybe too heavy"),
    ("AK-12",34,30,80,750,"assault",700,"You grab the AK-12. You know this gun. It's like the '47', but more balanced. In theory"),
    ("Fal 50.0",49,20,75,400,"assault",1000,"You pick up the FAl 50.0. It takes 7.62x51mm Nato rounds. A Beast, hopefully"),
    ("AUG A3",32,30,90,850,"assault",1400),
    ("P90",24,50,60,1100,"smg",1200),
    ("G11",15,33,65,2100,"assault",2600),


]

for i in weapon_data:

    weapons.append(Weapon(*i))



def main():
    print("Welcome to the game of something hopefully cool")



