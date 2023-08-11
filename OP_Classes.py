#This file is to create the Pirate and Captain classes of the One Piece Text Game. We will import this file over into the main script so we can play our game.

class Pirate:
    #We will start off with making the pirate class. Pirates will need a name, type of fighter, and level. We will determine max health based off it's level.
    #Starting health will be it's maxed health and the pirate begins not knocked out.
    def __init__(self, name, fighter_type, level = 10):
        self.name = Name
        self.fighter_type = fighter_type
        self.level = level
        self.health = level * 5
        self.max_health = level * 5
        self.is_knocked_out = False

    def __repr__(self):
        #Whenever you print a Pirate to the console, it will tell you their name, fighter type, level, and how much health they have left.
        return "Your {0} level pirate, {1}, has {2} health remaining. {1} is a {3} fighting type pirate.".format(level, name, health, fighter_type)

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
        print("Your pirate {0} now has {1} health! Back to the fight!".format(name, health)

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
            print("{0} attacked {1} for {2} damage!".format(self.name, enemy_pirate.name, round(self.level * 0.5))
            print("That attack could have done more. Keep trying!")
            enemy_pirate.lose_health(round(self.level * 0.5))

        #Same Type
        if (self.fighter_type == "Devil Fruit" and enemy_pirate.fighter_type == "Devil Fruit") or (self.fighter_type == "Sword" and enemy_pirate.fighter_type == "Sword") or (self.fighter_type == "Haki" and enemy_pirate.fighter_type == "Haki"):
            print("{0} attacked {1} for {2} damage!".format(self.name, enemy_pirate.name, self.level))

            

       


    






