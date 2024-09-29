print("Welcome to Treasure Island \nYour mission is to find the treasure. \nYou're at a cross road. Where do you want to go?")
user_choice1 = input(' Type "left" or "right" \n').lower()
if user_choice1 == "left":
    user_choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake.'
                         ' Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    if user_choice2 == "wait":
        user_choice3 = input("You arrive at the island unharmed. There is a house with 3 doors."
                             " One red, one yellow and one blue. Which colour do you choose?\n").lower()
        if user_choice3 == "red":
                print("You found the treasure. You win")
        elif user_choice3 == "yellow":
                print("You Lost.")
        elif user_choice3 == "blue":
                print("You Lost.")
    else:
        print("You Lost.")
else: 
    print("You Lost.")