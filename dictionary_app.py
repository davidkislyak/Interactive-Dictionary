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

            # for each close match found:
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


# ask user for input and save to variable: user_input
user_input = input("What word would you like to look up the definition for: ")

# Call function word_lookup and save response to variable: definition
definition = word_lookup(user_input)

# for each different definition returned:
for i in definition:
    print("\n" + str(i))

# Keep program from automatically closing
input()
