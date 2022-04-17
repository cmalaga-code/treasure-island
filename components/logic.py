def first_trial():
    user_left_or_right = input("You have to make a choice. Do you want to go left or right ? type 'left' or type 'right' \n").lower()
    if user_left_or_right == "left" or user_left_or_right == "right":
        if user_left_or_right == "left":
            return False
        else:
            return True
    else:
        raise Exception("You need to type 'left' or 'right' .. ")

def second_trial():
    user_swim_river = input("You have to make a choice. Do you want to swim to the treasure ? type 'yes' or 'no' \n").lower()
    if user_swim_river == "yes" or user_swim_river == "no":
        if user_swim_river == "yes":
            return False
        else:
            return True
    else:
        raise Exception("You need to type 'yes' or 'no' .. ")

def thrid_trial():
    user_door_choice = input("You have to make a choice. Which door should you open ? type 'gold' or 'white' or 'green' \n").lower()
    if user_door_choice == "gold" or user_door_choice == "white" or user_door_choice == "green":
        if user_door_choice == "gold" or user_door_choice == "green":
            return False
        else:
            return True
    else:
        raise Exception("You need to type 'gold' or 'white' or 'green' .. ")