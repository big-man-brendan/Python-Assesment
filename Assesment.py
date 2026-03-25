import random


def battle(do_you_shoot_first, name):
    # Sets the enemy for ease of use. Will change to be random based on things later
    enemy = Enemy(name, random.randint(10000, 10000), [all_weapons[0]])

    # Just loop until someone dies
    while player.health > 0 and enemy.health > 0:

        # Only runs the first time if you can shoot first
        if do_you_shoot_first:

            print("What weapon do you want to use:\n")
            # List all the weapons that you have and let you pick one

            list_weapons()



            while not False:

                try:

                    choice = int(input("> "))

                    player_weapon = player.inv[choice - 1]

                    break

                except IndexError:
                    print("Theres no weapon there")
                except ValueError:
                    print("Please pick a proper number")

                print()

            # Sets the damage and bullets with the class func
            # and checks if you are reloading
            if player_weapon.ammo == 0:

                bullets_left = player.ammo_inv[player_weapon.bullet]

                spent_ammo = player_weapon.reload(True, bullets_left)

                player.ammo_inv[player_weapon.bullet] -= spent_ammo



            else:
                damage, bullets = player_weapon.shoot()
                enemy.health -= damage

                # Sets things health to zero if it's negative for nicer visuals
                if enemy.health < 0:
                    enemy.health = 0

                print(f"You shot {bullets} rounds for a total of {damage} damage")
                print(f"The {enemy.name} now has {enemy.health} health remaining")

            print()

        do_you_shoot_first = True

        if enemy.health <= 0:
            break

        # Picks a random weapon out of the enemy's inventory
        op_weapon = random.choice(enemy.weapons)

        # Just does the same thing as before but for the enemy
        if op_weapon.ammo == 0:
            op_weapon.reload(False, 10000)

        else:
            damage, bullets = op_weapon.shoot()
            player.health -= damage

            if player.health < 0:
                player.health = 0

            print(
                f"The {enemy.name} shot {bullets} rounds into you "
                f"for a total of {damage} damage"
            )
            print(f"You are now on {player.health} health")

        print()

    if player.health == 0:
        print("GAME OVER")
        main()


    else:

        # A 30 percent chance for the enemy to drop something random out of their inventory

        item_drop = 0

        if random.randint(1, 10) > 7:
            item_drop = random.choice(enemy.weapons)

        if item_drop:
            print(f"The {enemy.name} dropped an {item_drop.name}")

            CollectWeapon(item_drop)




        # make the enemy drop some ammo




def encounter(name):
    # Picks a random message and a random name for the encounter.
    # Example output:
    # You see a Bandit in an alley way

    random_names = ("Bandit", "Bastard", "Robber", "Thug", "Brute", "Foe", "Savage", "Matthew Chung")

    if not name:
        name = random.choice(random_names)

    random_text = (
        f"You see a {name} in an alley way",
        f"You spot a {name} hanging around",
        f"You see the head of a {name} poking out of a bush",
        f"A {name} looks at you for a little too long",
        f"You notice a {name} mugging someone",
        f"You see a {name} looking for trouble",
    )

    text = random.choice(random_text)
    print(text)

    # Lets you choose whether to fight or sneak past,
    # but if you sneak past there's a chance of getting caught
    # and then the enemy gets to shoot first
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

    # Sends you to the battle function depending on what you pressed,
    # and also makes the chance of getting caught
    if choice == "1":
        if random.randint(0, 1):
            print(f"You managed to successfully sneak past the {name}")

        else:
            print(f"The {name} caught you!!!")
            battle(False, name)

    if choice == "2":
        battle(True, name)


def list_weapons():

    print("   Weapon | Ammo | Total Ammo\n")

    for i in range(len(player.inv)):
        weapon = player.inv[i]
        print(f"{i + 1}: ", weapon.name, end=" | ")
        print(f"{weapon.ammo}", end=" | ")
        print(f"{player.ammo_inv[weapon.bullet]}", end="")

        if weapon.ammo == 0:
            print("  (RELOAD)")

        print()

    print()


def collect_weapon(weapon):

    weapon.pick_up()

    #You can only have 3 weapons so you have to drop one



    if len(player.inv) >= 3:

        print("You can only have 3 weapons")
        print("Which one do you want to drop")


        list_weapons()

        print(f"4: ", weapon.name, end=" | ")
        print(f"{weapon.ammo}", end=" | ")
        print(f"{player.ammo_inv[weapon.bullet]}", end="")
        print(" (new) ")


        while True:

            try:

                choice = int(input("> "))

                if choice == 4:
                    break

                choice = player.inv[choice-1]
                break


            except ValueError:
                print("Pick a number")
            except IndexError:
                print("Theres no weapon there")


        if choice == 4:
            pass

class Player:
    #Makes the player class, so it's easy to interact with the player.

    def __init__(self, name, health, inv, ammo_inv):
        self.name = name
        self.health = health
        self.inv = inv
        self.ammo_inv = ammo_inv


class Weapon:
    # Allows a lot of weapons to be made cleanly

    # Makes a random pickup verb so it's different each time
    pick_up_verbs = ["grab", "take", "lift", "secure", "shoulder"]

    def __init__(
            self, name, damage, clip_cap, accuracy, fire_rate, level, bullet, value,
            pickup_message, ammo
    ):
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
        # Add a bit of random variation so you might get slightly different damage each time
        variation = random.uniform(0.8, 1.2)
        bullets = (self.fire_rate / 60) * self.accuracy

        # Makes it so if you don't have many bullets left it does it properly
        bullets = min(round(bullets * variation), self.ammo)

        variation = random.uniform(0.9, 1.1)
        total_damage = round(variation * bullets * self.damage)
        self.ammo -= bullets

        return total_damage, bullets

    def pick_up(self):
        # Makes the random pickup thing.
        # Example output:
        # You lift the AK-47. Chambered in 7.62 blah blah blah
        verb = random.choice(self.pick_up_verbs)
        print(self.pickup_message.format(verb=verb))

    def reload(self, player_or_op, bullets_left):
        if bullets_left > 0:
            if player_or_op:
                print(f"You reload the {self.name}")
                print(f"{bullets_left} rounds goes into the weapon")

            else:
                print("The enemy reloads their weapon")

            self.ammo = min(bullets_left, self.clip_cap)

        else:
            if player_or_op:
                print("You don't have enough ammo to reload")

        return self.ammo


class Enemy:
    # A class for the enemy

    def __init__(self, name, health, weapons):
        self.name = name
        self.health = health
        self.weapons = weapons

    def attack(self):
        pass


class Item:
    # A class for items, which can be randomly picked up and sold for money

    def __init__(self, name, value):
        self.name = name
        self.value = value





# Makes the player with the player class
player = Player("Player", 9999999, [], {"assault": 0, "smg": 0, "shotgun": 0, "pistol": 0, "sniper": 0})

all_weapons = []

# Sets up all the weapons. Each one has a name, damage, and so on.
# The {verb} in the pick up message gets replaced randomly inside the class each time guns are picked up
weapon_data = [
    (
        "AK-47", 40, 30, 70, 650, 1, "assault", 500,
        "You {verb} the AK-47, Chambered in 7.62. It feels heavy in your hands. Maybe too heavy",
    ),
    (
        "AK-12", 34, 30, 80, 750, 1, "assault", 700,
        "You {verb} the AK-12. You know this gun. It's like the '47', but more balanced. In theory",
    ),
    (
        "Fal 50.0", 49, 20, 75, 400, 2, "assault", 1000,
        "You {verb} the FAl 50.0. It takes 7.62x51mm Nato rounds. A Beast, hopefully",
    ),
    (
        "AUG A3", 32, 30, 90, 850, 3, "assault", 1400,
        "You {verb} the AUG A3. The compact bullpup package, boasting supreme accuracy. ",
    ),
    (
        "P90", 24, 50, 60, 1300, 3, "smg", 1200,
        "Cold polymer meets your grip as you {verb} the P90. You see the 50 round box mag. Its ready to take on a hoard",
    ),
    (
        "G11", 15, 33, 65, 2100, 10, "assault", 2600,
        "As you {verb} the G11, you feel the spirit of West Germany. Experimental, desperate, and ahead of its time.",
    ),
]

# Simply adds all the guns as classes to a list,
# and repeats the ammo cap to be the current ammo
for i in weapon_data:
    all_weapons.append(Weapon(*i, i[2]))


def main():
    print("Welcome to the game of something hopefully cool")

    # Just some testing stuff. Temporary



    player.inv.append(all_weapons.pop(0))
    player.inv.append(all_weapons.pop(3))
    player.inv.append(all_weapons.pop(3))

    collect_weapon(all_weapons[2])

    player.ammo_inv["assault"] = 15

    battle(True, "Bastard")


main()

print("Garr")

# we have it like this
# [{ak_47_class:ammo_amount},{aug_a3_class:ammo_amount}]
# we need it like this
# [
