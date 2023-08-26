#This file is to create the Pirate and Captain classes of the One Piece Text Game. We will import this file over into the main script so we can play our game.

from imp import new_module
from os import name


class Pirate:
    #We will start off with making the pirate class. Pirates will need a name, type of fighter, and level. We will determine max health based off it's level.
    #Starting health will be it's maxed health and the pirate begins not knocked out.
    def __init__(self, name, fighter_type, level = 10):
        self.name = name
        self.fighter_type = fighter_type
        self.level = level
        self.health = level * 5
        self.max_health = level * 5
        self.is_knocked_out = False

    def __repr__(self):
        #Whenever you print a Pirate to the console, it will tell you their name, fighter type, level, and how much health they have left.
        return "Your {0} level pirate, {1}, has {2} health remaining. {1} is a {3} fighting type pirate.\n".format(level, name, health, fighter_type)

    def knockout(self):
        #During battle, knocking out an opposing pirate will change their knocked out status to True. A knocked out pirate can't have any health left.
        #So knockout should only be called if the pirate has 0 health. In case of error, the pirates health will be set to 0
        self.is_knocked_out = True
        if self.health is not 0:
            self.health == 0
        print("Your pirate {0} has been knocked out!".format(name))

    def revive(self):
        #Opposite of knockout, revive will change a pirate's knocked out status to False. Similar to above, a revived pirate must have at least 1 health so health will be set to 1.
        self.is_knocked_out = False
        if self.health is 0:
            self.health = 1
        print("Your pirate {0} has been revived! Thank goodness.".format(name))

    def lose_health(self, amount):
        #Function used to deduct health from pirates during battle. If pirate's health reaches 0, change knock out status to True
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            self.knockout()
        else:
            print("Your pirate {0} now only has {1} health! Watch out".format(name, health))

    def gain_health(self, amount):
        #Function used to add health to a pirate. If a pirate who's health is 0 gains health, change knocked out status to False
        if self.health == 0:
            self.revive()
        self.health += amount
        #Can't let the pirates come back with more health than their max health
        if self.health >= self.max_health:
            self.health = self.max_health
        print("Your pirate {0} now has {1} health! Back to the fight!".format(name, health))

    def attack(self, enemy_pirate):
        #Function used to actually fight in the game.
        #First need to check if your pirate is knocked out or not
        if self.is_knocked_out:
            print("{0} is knocked out and can no longer fight!".format(name))
            return

    
        #The rest of the attack function will deal with taking type advantages into consideration. Since this is based off the manga One Piece, the 3 types I will use will be Devil Fruit, Haki, and Sword.
        #While these are case-by-case in the One piece world, I am going to make my own type weakness triangle. Devil Fruit beats Sword. Sword beats Haki, and Haki beats Devil Fruit.
        #Attacks with advantage will have double damage and attacks with disadvantage will have half damage.

        #Super Effective
        if (self.fighter_type == "Devil Fruit" and enemy_pirate.fighter_type == "Sword") or (self.fighter_type == "Sword" and enemy_pirate.fighter_type == "Haki") or (self.fighter_type == "Haki" and enemy_pirate.fighter_type == "Devil Fruit"):
            print("{0} attacked {1} for {2} damage!".format(self.name, enemy_pirate.name, self.level * 2))
            print("It's super effective!")
            enemy_pirate.lose_health(self.level * 2)
      
        #Not Effective
        if (self.fighter_type == "Devil Fruit" and enemy_pirate.fighter_type == "Haki") or (self.fighter_type == "Haki" and enemy_pirate.fighter_type == "Sword") or (self.fighter_type == "Sword" and enemy_pirate.fighter_type == "Devil Fruit"):
            print("{0} attacked {1} for {2} damage!".format(self.name, enemy_pirate.name, round(self.level * 0.5)))
            print("That attack could have done more. Keep trying!")
            enemy_pirate.lose_health(round(self.level * 0.5))

        #Same Type
        if (self.fighter_type == "Devil Fruit" and enemy_pirate.fighter_type == "Devil Fruit") or (self.fighter_type == "Sword" and enemy_pirate.fighter_type == "Sword") or (self.fighter_type == "Haki" and enemy_pirate.fighter_type == "Haki"):
            print("{0} attacked {1} for {2} damage!".format(self.name, enemy_pirate.name, self.level))
            print("The pirates seem about even!")
            enemy_pirate.lose_health(self.level)

            
#Time to set up the Captain class. In this case, the Captain of the crew will be who controls the pirates and battles with them. 
#Captains have a name, list of their crew, and a number of rumble balls. Whenever the Captain gets initialized, the first pirate in their list will be their first mate aka the active one.
class Captain:
    def __init__(self, name, crew_list, num_rumble_balls):
        self.name = name
        self.crew = crew_list
        self.rumble_balls = num_rumble_balls
        self.first_mate = 0

    def __repr__(self):
        #Prints out your current stats as Captain. Name, what pirates are in your crew, and your current first mate
        print("The captain {0} has the following crew:".format(self.name))
        for pirates in self.crew:
            print(pirates)
        return "Your current first mate is {0}.format(self.crew[self.first_mate].name)"

    def switch_first_mate(self, new_mate):
        #Changes first mate to the number given as the new_mate parameter
        #First need to check if the number for the new_mate is valid, the crew mate isn't knocked out, and isn't your current first mate.
        if new_mate < len(self.crew) and new_mate >= 0:
            if self.crew[new_mate].is_knocked_out:
                print("{0} is knocked out! You can't make them your first mate.".format(self.crew[new_mate].name))
            elif new_mate == self.first_mate:
                print("{0} is already your current first mate.".format(self.crew[new_mate].name))
            else:
                self.first_mate = new_mate
                print("I'm counting on you, {0}!".format(self.crew[self.first_mate].name))

    def user_rumble_balls(self):
        #Uses one of the Rumble Balls Dr. Chopper cooked up to heal your crew and give them energy to fight again.
        if self.rumble_balls > 0:
            print('You used a rumbkle ball on {0}'.format(self.crew[self.first_mate].name))
            #A Rumble Ball restores 30 health to your first mate
            self.crew[self.first_mate].gain_health(30)
            self.rumble_balls -= 1
        else:
            print('Oh no! You are out of rumble balls!')

    def attack_other_captain(self, other_captain):
        #First mate fights the Other Captain's first mate
        my_first_mate = self.crew[self.first_mate]
        other_first_mate = other_captain.crew[other_captain.first_mate]
        my_first_mate.attack(other_first_mate)

       


    






