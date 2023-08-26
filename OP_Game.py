
import OP_Classes.py

#Giving the captains a handful of options to choose for their pirates

a = Pirate('Luffy', 'Devil Fruit', 7)
b = Pirate('Zoro', 'Sword', 8)
c = Pirate('Shanks', 'Haki', 10)
d = Pirate('BlackBeard', 'Devil Fruit', 8)
e = Pirate('Tsushigi', 'Sword', 4)
f = Pirate('Oden', 'Sword')

pirate_list = [a, b, c, d, e, f]

#Time to receive input from the players and let them choose their crew
captain_one_name = input('Welcome to the world of One Piece! Please enter your Captain name and press the enter key. ')
captain_two_name = input('Ahoy, ' + captain_one_name + '! Let\'s find your rival captain. Enter your rival\'s name and press enter.' )

crew_choice = input(str(captain_one_name) + (', it\'s time to choose your first crew member. Look at the list below and choose one.'))

print(pirate_list)

while crew_choice not in pirate_list:
    crew_choice = input('That is not one of the available pirates. Try again!')

#Keeping track of each captains team
captain_one_crew = []
captain_two_crew = []


    
