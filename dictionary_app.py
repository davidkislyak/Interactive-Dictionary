# dictionary_app.py
# David Kislyak
# 3/15/2018
# CLI dictionary application

import json
from difflib import SequenceMatcher, get_close_matches

data = json.load(open("data.json"))  # secretly is: open("data.json", "r")

def word_lookup(word):
    #__init__
    close_matches = []
    word = word.lower()

    # Attempt to look for the user input in the dictionary 
    try:
        definition_list = data[word]

    # If that fails and receives a KeyError:
    except KeyError:

        # Attempt to find similar words to the users word
        close_matches = get_close_matches(user_input, data.keys())

        # If there are no close_matches:
        if len(close_matches) == 0:
            return["I can't find that word. Please double check the word."]

        # If there is at least one close match:
        else:
            print("\nDid you mean: ")

            # For every close match found:
            for i in range(len(close_matches)):
                print(str(i + 1) + ".) " + str(close_matches[i]).capitalize())
            print("0.) My word is not on here")

            # Gather user input about word selection and subtract one to index properly
            user_correct_word = int(input("\nWhat is your word: ")) - 1

            # If user selected that the word is not on the list:
            if user_correct_word == - 1:
                return["Sorry I guess I can't find that word."]

            # If the user has picked a word from the list:
            elif user_correct_word <= len(close_matches) - 1:
                return data[close_matches[user_correct_word]]

            # If the user has entered a non existent index:
            else:
                return["Sorry that option does not exist."]
            
    return definition_list


# Ask user for input and save to variable: user_input
user_input = input("What word would you like to look up the definition for: ")

# Call function word_lookup and save response to variable: definition
definition = word_lookup(user_input)

# For each different definition returned:
for i in definition:

    # If the response is less than 104 characters:
    if len(i) <= 103:
        print("\n" + str(i))

    # Else if character count > 104
    else:

        # Create Temporary variables 
        temp_list = []
        character_count = 0
        final_string = ""

        # Split the current sentence into a list of words (using spaces)
        temp_list = i.split(" ")

        # For each index (word) in temp_list:
        for x in temp_list:

            # Set character_count to the length of the word
            character_count += len(x)

            # If the amount of characters on the current line is less than 103:
            if character_count <= 103:
                final_string += " " + str(x)

            # If the amount of characters printed on the current is more than 103:
            elif character_count >= 103:
                #               Start new line
                final_string += "\n" + str(x)
                # Reset character counter because a new line has started
                character_count = 0

            else:
                character_count += len(x)
                final_string += " " + str(x)

        # Print out the end result    Remove whitespace
        print("\n" + str(final_string).strip())


# Keep program from automatically closing
input()
