import random
import time


def start():

    print("You wake up. Your in a cave, and remember nothing.")
    time.sleep(0.2)
    print("Theres dust in your eye's, and you can barely make out something")
    time.sleep(0.2)
    print("A Kalashnikov AK-47")
    time.sleep(0.5)
    print("Fully loaded and ready to go")
    time.sleep(0.2)
    print("You walk out of the cave, and see the city")
    time.sleep(0.2)
    print("Then you remember. The man who killed your family")
    time.sleep(0.2)
    print("You have to chase him")

    player.inv.append(all_weapons.pop(0))


def battle(do_you_shoot_first, name):
    # Sets the enemy for ease of use. Will change to be random based on things later

    enemy = Enemy(name, random.randint(700, 1400), [random.choice(all_weapons)])

    # Just loop until someone dies
    while player.health > 0 and enemy.health > 0:

        # Only runs the first time if you can shoot first
        if do_you_shoot_first:

            print("What weapon do you want to use:\n")
            # List all the weapons that you have and let you pick one

            list_weapons(player.inv)

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
        time.sleep(1)
        main()


    else:

        player.health = 1000

        # A 70 percent chance for the enemy to drop something random out of their inventory
        # then if not then they will drop an item


        if name == "Beast":
            return

        item_drop = 0

        if random.randint(1, 10) > 3:
            item_drop = random.choice(enemy.weapons)

        if item_drop:
            print(f"The {enemy.name} dropped an {item_drop.name}")

            collect_weapon(item_drop)


        else:

            item_drop = random.choice(heaps_of_items)

            print(f"The {enemy.name} dropped a {item_drop.name}. Its worth ${item_drop.value} bucks")

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


def boss_fight():

    print()
    print("You walk in to chamber. You here the laughs of a great voice echoing on the walls")
    time.sleep(0.5)



    print("'Congratulations' Says a booming voice")
    time.sleep(0.5)

    print("You have passed my test. But now you die")


    battle(False,"Beast")

    
    print("'Arrrrr'")
    time.sleep(1)
    


def list_weapons(inv):
    print("   Weapon | Ammo | Total Ammo\n")

    for i in range(len(inv)):
        weapon = inv[i]
        print(f"{i + 1}: ", weapon.name, end=" | ")
        print(f"{weapon.ammo}", end=" | ")
        print(f"{player.ammo_inv[weapon.bullet]}", end="")

        if weapon.ammo == 0:
            print("  (RELOAD)")

        print()


def collect_weapon(weapon):
    weapon.pick_up()

    # You can only have 3 weapons so you have to drop one

    if len(player.inv) >= 3:

        print()
        print("You can only have 3 weapons")
        print("Which one do you want to drop")
        print()

        list_weapons(player.inv)

        print(f"4: ", weapon.name, end=" | ")
        print(f"{weapon.ammo}", end=" | ")
        print(f"{player.ammo_inv[weapon.bullet]}", end="")
        print(" (new) ")

        print()

        while True:

            try:

                choice = int(input("> "))
                print()
                if choice == 4:
                    break

                choice = player.inv[choice - 1]
                break


            except ValueError:
                print("Pick a number")
            except IndexError:
                print("Theres no weapon there")
            print()

        if choice == 4:

            print(f"You got rid of the {weapon.name}")


        else:

            print(f"You dropped your {choice.name}")

            player.inv.remove(choice)

            player.inv.append(weapon)

    else:
        player.inv.append(weapon)


def shop():
    def buy_ammo(type, amount, price):

        if player.money >= price:

            print("Do you want to buy\n1: Yes\n2: No")

            while True:

                try:

                    choice = int(input("> "))

                    if choice in (1, 2):
                        break

                    else:
                        print("Enter a proper number")


                except ValueError:
                    print("Enter a number")

            if choice == 1:
                player.money -= price

                player.ammo_inv[type] += amount

    print("Welcome to Matthew Chung's shop")

    print("What do you want to do:\n")

    while True:

        print("1: Buy Guns\n2: Buy Ammo\n3: Exit\n")

        while True:
            try:

                choice = int(input("> "))

                if choice in (1, 2, 3):
                    break

                else:
                    print("You have to pick a option")

            except ValueError:
                print("Pick a number")

        print()

        if choice == 1:

            products = []
            products_index = []

            for _ in range(5):
                index = random.randint(0, len(all_weapons) - 1)

                products_index.append(index)

                products.append(all_weapons[index])

            print(f"You have ${player.money}.00")

            for i in range(len(products)):
                weapon = products[i]
                print(f"{i + 1}: ", weapon.name, end=" | ")

                print(f"${weapon.value}", end="")
                print()

            print("6:  Exit")

            while True:

                try:

                    choice = int(input("> "))

                    if choice in (1, 2, 3, 4, 5, 6):
                        break

                    else:
                        print("Pick a proper number")
                except ValueError:
                    print("Pick a number")

            if choice == 6:
                pass


            else:

                weapon = products[choice - 1]

                print()
                print(f"You have ${player.money}.00")
                print(f"This one cost ${weapon.value}")
                print()
                if player.money < weapon.value:
                    print("You can't afford it")

                else:

                    print("Do you want to buy")
                    print("1: Yes\n2: No")

                    while True:
                        try:

                            choice = int(input("> "))

                            if choice in (1, 2):
                                break

                            else:
                                print("Enter a proper number")

                        except ValueError:
                            print("Enter a number")

                    if choice == 1:
                        all_weapons.remove(weapon)

                        player.money -= weapon.value

                        collect_weapon(weapon)

                    if choice == 2:
                        pass




        elif choice == 2:
            print("Buy Ammo")

            print("What do you want to buy do you want to buy:")
            print()
            print("       Ammo | Your Ammo")

            print(f"1: Assault: {player.ammo_inv['assault']}")
            print(f"2: SMG: {player.ammo_inv['smg']}")
            print(f"3: Shotgun: {player.ammo_inv['shotgun']}")
            print(f"4: Pistol: {player.ammo_inv['pistol']}")
            print(f"5: Sniper: {player.ammo_inv['sniper']}")
            print("6: Exit")

            while True:

                try:

                    choice = int(input("> "))

                    if choice in (1, 2, 3, 4, 5, 6):
                        break

                    else:
                        print("Enter a proper number")

                except ValueError:
                    print("Enter a number")

            print(f"You have ${player.money}.00")

            print("You can get ", end='')

            match choice:

                case 1:

                    print("30 rifle rounds for $100 Dollars")

                    buy_ammo("assault", 30, 100)

                case 2:

                    print("60 smg rounds for $100 Dollars")
                    buy_ammo("smg", 60, 100)

                case 3:
                    print("12 shotgun shells for $100 Dollars")
                    buy_ammo("shotgun", 12, 100)

                case 4:

                    print("48 pistol shots for 100 dollars")
                    buy_ammo("pistol", 48, 100)

                case 5:

                    print("8 round for 100 dollars")
                    buy_ammo("sniper", 8, 100)

                case 6:

                    pass

            print()

            print()


        elif choice == 3:
            return


def menu():

    level = 0

    while True:
        
        print("1: Proceed forward\n2: Check Inventory\n3: Shop\n4: Restart")

        while True:
            try:

                choice = int(input("> "))

                if choice in (1, 2, 3):
                    break

                else:
                    print("Pick an option")

            except ValueError:
                print("Enter a number")

        match choice:

            case 1:
                
                
                if level == 10:

                    boss_fight()

                encounter(0)
                level += 1

            #case 2:
             #   print("Inventory")

            case 2:
                shop()

            case 3:
                main()


class Player:
    # Makes the player class, so it's easy to interact with the player.

    def __init__(self, name, health, inv, ammo_inv, money):
        self.name = name
        self.health = health
        self.inv = inv
        self.ammo_inv = ammo_inv
        self.money = money


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


def main():

    start()

    boss_fight()

    menu()


# just a list for a bunch of random items to drop
heaps_of_items = [
    Item("Broken gun", 40),
    Item("Spoon", 5),
    Item("Rusty bolt", 2),
    Item("Roll of duck tape", 15),
    Item("Empty bottle", 1),
    Item("Crumpled note", 2),
    Item("Old phone", 25),
    Item("Scrap metal", 12),
    Item("Loose screw", 1),
    Item("Torn backpack", 18),
    Item("Car battery", 60),
    Item("Glass shard", 4),
    Item("Oil can", 20),
    Item("Used bandage", 6),
    Item("Broken watch", 10),
    Item("Random key", 8),
    Item("Metal pipe", 35),
    Item("Worn glove", 14),
    Item("Flashlight", 22),
    Item("Kitkat", 2),
    Item("Circuit board", 45),
    Item("Can of beans", 7),
    Item("Radio", 55),
]

# Makes the player with the player class
player = Player("Player", 1000, [], {"assault": 100, "smg": 100, "shotgun": 20, "pistol": 60, "sniper": 10}, 10000)

# Sets up all the weapons. Each one has a name, damage, and so on.
# The {verb} in the pick up message gets replaced randomly inside the class each time guns are picked up

all_weapons = []

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
    (   "NTW-20", 600, 1, 95, 30, 10, "sniper", 6000,
        "You {verb} the NTW-20. A monster of a gun. You can barely handle it. You feel bad for its future victims",
     ),
    (
        "Remington 870", 70, 8, 50, 200, 1, "shotgun", 400,
        "You {verb} the Remington 870. A classic pump action shotgun. Reliable, and unbreakable. Maybe a bit simple."

    ),
    (   "Zip 22", 3, 10, 40, 300, 10, "pistol", 10000,
        "As you {verb} the Zip 22, you feel the power of the beast. 10 Grand, worth every penny."

     ),
    (   "Famas F1", 32, 25, 65, 1100, 2, "assault", 1100,
        "You {verb} the Famas F1. The French bullpup. It looks weird, and shoots weird, but effective nonetheless."

     ),
    (   "M4A1", 33, 30, 80, 900, 2, "assault", 900,
        "'The most boring gun in the world', you think as you {verb} the M4A1."
     ),
    (  "Remington 700", 130, 7, 90 , 150 , 5, "sniper", 1200,
        "The Remington 700. A classic sniper rifle. You {verb} it and check the magazine"
    )

]

# Simply adds all the guns as classes to a list,
# and repeats the ammo cap to be the current ammo
for i in weapon_data:
    all_weapons.append(Weapon(*i, i[2]))

main()

print("Finished")

# we have it like this
# [{ak_47_class:ammo_amount},{aug_a3_class:ammo_amount}]
# we need it like this
# [
