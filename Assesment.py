import random



def battle(do_you_shoot_first, name):

    # Sets the enemy for ease of use. will change to be random based on things later
    enemy = Enemy(name, random.randint(10000, 10000), [all_weapons[0]])

    # just loop intull someone dies
    while player.health > 0 and enemy.health > 0:


        # only runs the first time if you can shoot first
        if do_you_shoot_first:

            print("What weapon do you want to use:\n")

            # list all the weapons that you have and let you pick one

            print("   Weapon | Ammo | Total Ammo\n")


            for i in range(len(player.inv)):


                weapon = player.inv[i]

                print(f"{i + 1}: ", weapon.name,end = ' | ')
                print(f"{weapon.ammo}",end = ' | ')
                print(f"{player.ammo_inv[weapon.bullet]}",end = '')

                if weapon.ammo == 0:
                    print("  (RELOAD)")


            print()

            choice = int(input("> "))

            player_weapon = player.inv[choice - 1]

            # Sets the damage and bullets with the class func
            #and checks if you are reloading

            if player_weapon.ammo == 0:

                bullets_left = player.ammo_inv[player_weapon.bullet]

                player_weapon.reload(True,bullets_left)

                player.ammo_inv[player_weapon.bullet] -= player_weapon.ammo


            else:



                damage, bullets = player_weapon.shoot()



                enemy.health -= damage

                # Sets things health to zero if its negative for nicer visuals
                if enemy.health < 0:
                    enemy.health = 0

                print(f"You shot {bullets} rounds for a total of {damage} damage")
                print(f"The {enemy.name} now has {enemy.health} health remaining")

            print()

        do_you_shoot_first = True

        if enemy.health <= 0:
            break



        # picks a random weapon out of the enemys inventory
        op_weapon = random.choice(enemy.weapons)

        # just does the same thing as before but for the enemy.

        if op_weapon.ammo == 0:

            op_weapon.reload(False,10000)



        else:

            damage, bullets = op_weapon.shoot()


            player.health -= damage

            if player.health < 0:
                player.health = 0

            print(f"The {enemy.name} shot {bullets} rounds into you for a total of {damage} damage")
            print(f"You are now on {player.health} health")


        print()


    if player.health == 0:
        print("GAME OVER")

    # A 30 percent chance for the enemy to drop something random out of their inventory
    item_drop = 0

    if random.randint(1, 10) > 7:
        item_drop = random.choice(enemy.weapons)

    print("You won the fight!!")

    if item_drop:

        print(f"The {enemy.name} dropped an {item_drop.name}")
        player.inv.append(item_drop)



    else:
        print(f"The {enemy.name} didn't drop anything")


def encounter(name):

    # picks a random message and a random name for the encounter.
    # example output:
    # You see a Bandit in an alley way

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
    print(random_text)

    # Lets you choose wether to fight or sneak past,
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

    # Just sends you to the battle function depending on what you pressed, and also makes the chance of getting caught

    if choice == "1":

        if random.randint(0, 1):

            print(f"You managed to successfully sneak past the {name}")

        else:
            print(f"The {name} caught you!!!")

            battle(False, name)

    if choice == "2":
        battle(True, name)


# Makes the player class, so its easy to interact with the player.

class Player:
    def __init__(self, name, health, inv,ammo_inv):
        self.name = name
        self.health = health
        self.inv = inv
        self.ammo_inv = ammo_inv


# Allows a lot of weapons to be made cleanly.

class Weapon:

    # Makes a random pickup verb so its different each time
    pick_up_verbs = ["grab", "take", "lift", "secure", "shoulder"]

    def __init__(self, name, damage, clip_cap, accuracy, fire_rate, level, bullet, value, pickup_message,ammo):
        self.name = name
        self.damage = damage
        self.clip_cap = clip_cap
        self.accuracy = accuracy / 100
        self.fire_rate = fire_rate
        self.bullet = bullet
        self.value = value
        self.pickup_message = pickup_message
        self.level = level
        self.ammo = ammo

    def shoot(self):
        # Calculate how much damage is done per turn.
        # and add a bit of random variation so you might get slighty diffrent damage and stuff each time




        variation = random.uniform(0.8, 1.2)

        bullets = (self.fire_rate / 60) * self.accuracy

        #makes it so if you have not much bullets left it does it properly

        bullets = min(round(bullets * variation),self.ammo)

        variation = random.uniform(0.9, 1.1)

        total_damage = round(variation * bullets * self.damage)

        self.ammo -= bullets

        return total_damage, bullets

    def pick_up(self):
        # Makes the random pickup thing.
        # example output:
        # You lift the AK-47. Chambered in 7.62 blah blah blah

        verb = random.choice(self.pick_up_verbs)

        print(self.pickup_message.format(verb=verb))


    def reload(self,player_or_op,bullets_left):

        if bullets_left > 0:

            if player_or_op:

                print(f"You reload the {self.name}")
                print(f"{bullets_left} rounds goes into the weapon")

            else:
                print(f"The enemy reloads their weapon")

            self.ammo = min(bullets_left,self.clip_cap)

        else:
            if player_or_op:

                print("You don't have enough ammo to reload")


# A class for the enemy.
# I might not end up using it

class Enemy:
    def __init__(self, name, health, weapons):
        self.name = name
        self.health = health
        self.weapons = weapons

    def attack(self):
        pass


# A class for items, which can be randomly picked up at points and can be sold for money.

class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value


# Makes the player with the player class
player = Player("Player", 9999999, [],{"assault":0,"smg":0})

all_weapons = []

# Sets up all the weapons, each one has a name, damage and so on.
# The {verb} in the pick up message gets replaced randomly inside the class each time guns are picked up

weapon_data = [

    ("AK-47", 40, 30, 70, 650, 1, "assault", 500,
     "You {verb} the AK-47, Chambered in 7.62. It feels heavy in your hands. Maybe too heavy"),
    ("AK-12", 34, 30, 80, 750, 1, "assault", 700,
     "You {verb} the AK-12. You know this gun. It's like the '47', but more balanced. In theory"),
    ("Fal 50.0", 49, 20, 75, 400, 2, "assault", 1000,
     "You {verb} the FAl 50.0. It takes 7.62x51mm Nato rounds. A Beast, hopefully"),
    ("AUG A3", 32, 30, 90, 850, 3, "assault", 1400,
     "You {verb} the AUG A3. The compact bullpup package, boasting supreme accuracy. "),
    ("P90", 24, 50, 60, 1100, 3, "smg", 1200,
     "Cold polymer meets your grip as you {verb} the P90. You see the 50 round box mag. Its ready to take on a hoard"),
    ("G11", 15, 33, 65, 2100, 10, "assault", 2600,
     "As you {verb} the G11, you feel the spirit of West Germany. Experimental, desperate, and ahead of its time."),

]

# Simply adds all the guns as classes to a list. and repeats the ammo cap to be the current ammo

for i in weapon_data:
    all_weapons.append(Weapon(*i,i[2]))


def main():
    print("Welcome to the game of something hopefully cool")


# Just some testing stuff. temporary




player.inv.append(all_weapons.pop(0))


battle(True, "Bastard")

main()



#we have it like this

#[{ak_47_class:ammo_amount},{aug_a3_class:ammo_amount}]

#we need it like this

#[
