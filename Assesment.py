import random
import time

class Player:
    def __init__(self, name, health,inv):
        self.name = name
        self.health = health
        self.inv = inv


class Weapon:


    pick_up_verbs = ["grab", "take", "lift", "secure", "shoulder"]

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

        verb = random.choice(self.pick_up_verbs)


        slow_text(self.pickup_message.format(verb= verb))


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

    for letter in str(text):
        print(letter,end = '',flush= True)

        if letter in (",",".","!",":","?"):
            time.sleep(0.1)

        else: time.sleep(0.03)



all_weapons = []

weapon_data = [

    ("AK-47",40,30,70,650,"assault",500,"You {verb} the AK-47, Chambered in 7.62. It feels heavy in your hands. Maybe too heavy"),
    ("AK-12",34,30,80,750,"assault",700,"You {verb} the AK-12. You know this gun. It's like the '47', but more balanced. In theory"),
    ("Fal 50.0",49,20,75,400,"assault",1000,"You {verb} up the FAl 50.0. It takes 7.62x51mm Nato rounds. A Beast, hopefully"),
    ("AUG A3",32,30,90,850,"assault",1400,"You {verb} the AUG A3. The compact bullpup package, boasting supreme accuracy. "),
    ("P90",24,50,60,1100,"smg",1200,"Cold polymer meets your grip as you {verb} the P90. You see the 50 round box mag. Its ready to take on a hoard"),
    ("G11",15,33,65,2100,"assault",2600,"As you {verb} the G11, you feel the spirit of West Germany. Experimental, desperate, and ahead of its time."),


]

for i in weapon_data:

    all_weapons.append(Weapon(*i))



def main():
    print("Welcome to the game of something hopefully cool")





current_weapon = all_weapons[random.randint(0,len(all_weapons)-1)]

print(current_weapon)

current_weapon.pick_up()


main()