
import OP_Classes

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

crew_choice = input(captain_one_name + ', it\'s time to choose your first crew member. Look at the list below and choose one.')

print(pirate_list)

while crew_choice not in pirate_list:
    crew_choice = input('That is not one of the available pirates. Try again!')

#Keeping track of each captains team
captain_one_crew = []
captain_two_crew = []

captain_one_crew.append(crew_choice)
pirate_list.pop(crew_choice)

#2nd captains turn
crew_choice = input('Now it\'s ' + captain_two_name + '\'s turn to choose.')

print(pirate_list)

captain_two_crew.append(crew_choice)
pirate_list.pop(crew_choice)

#Repeat for remaining pirates
crew_choice = input(captain_one_name + ', choose your second pirate.')

captain_one_crew.append(crew_choice)
pirate_list.pop(crew_choice)

crew_choie = input(captain_two_name + ', choose your second pirate.')

captain_two_crew.append(crew_choice)
pirate_list.pop(crew_choice)

crew_choice = input(captain_one_name + ', choose your final pirate.')

captain_one_crew.append(crew_choice)
pirate_list.pop(crew_choice)

print('That means' + captain_two_name + 'gets ' + pirate_list[0].name + " as their crew member.\n Now it\'s time to fight!")

captain_two_crew.append(pirate_list[0])

#Creating the Captain objects with the given names and crew list
captain_one = Captain(captain_one_crew, 3, captain_one_name)
captain_two = Captain(captain_two_crew, 3, captain_two_name)

print('It\'s time to decide the King of the Pirates! Here are the rivals fighting for the title!')

print(captain_one)
print(captain_two)

#Time to start the battle. While loop to keep the captains picking options until one is defeated.

while True:
    battle_choice = input(captain_one_name + ', choose what you would like to do:\n a: Attack\n b: Use Rumble Ball \n c: Change Pirate')

    if battle_choice == 'a':
        captain_one.attack_other_captain(captain_two)
    elif battle_choice == 'b':
        captain_one.use_rumble_ball()
    elif battle_choice == 'c':
        first_mate_choice = input('Choose between or 2nd and 3rd pirates by choosing 2 or 3')
        if first_mate_choice == '2':
            captain_one.switch_first_mate(2)
        if first_mate_choice == '3':
            captain_one.switch_first_mate(3)

    battle_choice = input(captain_two_name + 'It is your turn. Choose what you would like to do:\n a: Attack\n b: Use Rumble Ball \n c: Change Pirate')

    if battle_choice == 'a':
        captain_two.attack_other_captain(captain_one)
    elif battle_choice == 'b':
        captain_two.use_rumble_ball()
    elif battle_choice == 'c':
        first_mate_choice = input('Choose between or 2nd and 3rd pirates by choosing 2 or 3')
        if first_mate_choice == '2':
            captain_two.switch_first_mate(2)
        if first_mate_choice == '3':
            captain_two.switch_first_mate(3)




    
