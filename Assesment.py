import random
import time


def battle(do_you_shoot_first):
    pass

def encounter(name):

    #picks a random message and a random name for the encounter.
    #example output:
    #You see a Bastard in an alley way

    random_names = ("Bandit", "Bastard", "Robber", "Thug", "Brute", "Foe", "Savage")


    if not name:
        name = random.choice(random_names)

    random_text = (

        f"You see a {name} in an alley way",
        f"You spot a {name} hanging around",
        f"You see the head  of a {name} poking out of a bush",
        f"A {name} looks at you for a little to long",
        f"You notice a {name} mugging someone",
        f"You see a {name} looking for trouble",
    )

    text = random.choice(random_text)
    slow_text(random_text)

    #Lets you choose wether to fight or sneak past,
    # but  if you sneak past there's a chance of you getting caught and then the enemy gets to shoot first

    while True:

        print("You can try to sneak past. Or fight!")
        choice = str(input("Press 1 to sneak past, or 2 to Fight!\n> ")).strip()

        if choice == "1":
            print("You chose to sneak past")
            break

        elif choice == "2":
            print("You chose to Fight!")
            break

        else:
            print("You must pick a valid option")


    #Just sends you to the battle function depending on what you pressed, and also makes the chance of getting caught

    if choice == "1":

        if random.randint(0,1):

            slow_text(f"You managed to successfully sneak past the {name}")

        else:
            print(f"The {name} caught you!!!")

            battle(False)

    if choice == "2":

        battle(True)





def slow_text(text):

    #Just makes the text come out a bit slower, and makes it so punctuation has a little more delay


    for letter in str(text):
        print(letter,end = '',flush= True)

        if letter in (",",".","!",":","?"):
            time.sleep(0.1)

        else: time.sleep(0.03)








#Makes the player class, so its easy to interact with the player.

class Player:
    def __init__(self, name, health,inv):
        self.name = name
        self.health = health
        self.inv = inv


#Allows heaps of weapons to be made cleanly.
class Weapon:


    #Makes a random pickup verb so its different each time
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

        #Makes the random pickup thing.
        #example output:
        #You lift the AK-47. Chambered in 7.62 blah blah blah

        verb = random.choice(self.pick_up_verbs)


        slow_text(self.pickup_message.format(verb= verb))

#A class for the enemy.
#I might not end up using it

class Enemy:
    def __init__(self,name,health,weapon):
        self.name = name
        self.health = health
        self.weapon = weapon

    def attack(self):
        pass

#A class for items, which can be randomly picked up at points and can be sold for money.

class Item:
    def __init__(self,name,value):
        self.name = name
        self.value = value


#Makes the player with the player class
player = Player("Player",1000,[])



all_weapons = []

#Sets up all the weapons, each one has a name, damage and so on.
#The {verb} in the pick up message gets replaced randomly inside the class each time guns are picked up

weapon_data = [

    ("AK-47",40,30,70,650,"assault",500,"You {verb} the AK-47, Chambered in 7.62. It feels heavy in your hands. Maybe too heavy"),
    ("AK-12",34,30,80,750,"assault",700,"You {verb} the AK-12. You know this gun. It's like the '47', but more balanced. In theory"),
    ("Fal 50.0",49,20,75,400,"assault",1000,"You {verb} the FAl 50.0. It takes 7.62x51mm Nato rounds. A Beast, hopefully"),
    ("AUG A3",32,30,90,850,"assault",1400,"You {verb} the AUG A3. The compact bullpup package, boasting supreme accuracy. "),
    ("P90",24,50,60,1100,"smg",1200,"Cold polymer meets your grip as you {verb} the P90. You see the 50 round box mag. Its ready to take on a hoard"),
    ("G11",15,33,65,2100,"assault",2600,"As you {verb} the G11, you feel the spirit of West Germany. Experimental, desperate, and ahead of its time."),


]

#Simple adds all the guns as classes to a list

for i in weapon_data:

    all_weapons.append(Weapon(*i))



def main():
    print("Welcome to the game of something hopefully cool")


main()
