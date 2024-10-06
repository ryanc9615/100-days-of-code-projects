## Import files
import hangman_words
import hangman_art
import random

## Print logo
print(hangman_art.logo)

# Track the number of lives 

lives = 6

## Word Choice 

chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)

## User Choice 

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

## User to guess again 

# game_over variable act as control for loop. 
game_over = False
# empty list - used to keep track of correctly guessed letters by the user. Logical Flow. 
correct_letters = []

#Start while loop to prompt user to guess until the game is over. 
while not game_over:

    print(f"****************************{ lives}/6 LIVES LEFT****************************")
#User_input allows for the users guess. 
    user_input = input("Guess a letter: ").lower()
    
# Already Guessed 
    if user_input in correct_letters:
        print(f"You've already guessed {user_input}")
    
# Creates an empty string to show the current progress of guessed word. With respective positions and underscores for letters that haven't been guessed. 
    display = ""

   

# Starts for loop that iterates over the strings in chosen_word
    for letter in chosen_word:
#Check to see if current letter is equal to users input
        if letter == user_input:
# if true letter is added to the display string
          display += letter
# if true letter is added to the correct_letter list
          correct_letters.append(user_input)
# checks if current letter has already been correctly guessed before (i.e. present in the current_letters list)
        elif letter in correct_letters:
# if true the letter is added to the display string 
            display += letter
# incorrect or not guessed before will add an underscore
        else:
            display += "_"
    print(f"Word to guess: {display}")


# if the user guess is not found in the chosen word then reduce lives by 1 until the lives variable is equal to 0 then set the game_over value to equal True and 
#print you lose
    if user_input not in chosen_word:
        lives -= 1
        print(f"You guessed {user_input}, that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")


# checks if no more underscores are in the display variable meaning that all the letters in chosen_word have been guessed correctly. 
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")
    
    print(hangman_art.stages[lives])