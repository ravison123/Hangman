# Write your code here
import random
import sys
print('H A N G M A N')
print('There are currently 7 words in the database:')
print('python, java, kotlin, javascript, ravindra, advik, madhuri')
while True:
    list_ = ['python', 'java', 'kotlin', 'javascript', 'ravindra', 'madhuri', 'advik']      # This list can be added to include more names
    user_choice_play = input('Type "play" to play the game, "exit" to quit:')
    if user_choice_play == 'exit':
        break
    elif user_choice_play != 'play':
        continue
    choice = random.choice(list_)
    choice_set = set(choice)                # Creating a set of the letters in randomly chosen name by computer (Sets are computationaly light as compared to lists
    choice_to_print = '-' * len(choice)     # Initial string to print with all letters as -
    attempts = 0
    correct_choices = set()
    incorrect_choices = set()
    while True:
        print("")
        print(choice_to_print)
        user_char_choice = input('Input a letter:')
        if len(user_char_choice) > 1 or len(user_char_choice) == 0:
            print('You should input a single letter')
            continue
        if not user_char_choice.islower():
            print('It is not an ASCII lowercase letter')
            continue
        if user_char_choice not in choice_set and user_char_choice not in incorrect_choices:
            print('No such letter in the word')
            attempts += 1
            incorrect_choices.add(user_char_choice)
        else:
            if user_char_choice in correct_choices or user_char_choice in incorrect_choices:    # If letters are repeated by user
                print('You already typed this letter')
            else:                           #Block of code for replacing the - with guessed characters
                correct_choices.add(user_char_choice)
                index = 0
                while index < len(choice):
                    index = choice.find(user_char_choice, index)
                    if index == -1:         # -1 : the character is not found
                        break
                    choice_to_print = choice_to_print[:index] + user_char_choice + choice_to_print[index+1:]
                    index = index + 1
        if (choice_to_print == choice):
            print('You guessed the word {}!'.format(choice))
            print('You survived!')
            break
        if attempts == 8:
            print('You are hanged!')
            break
