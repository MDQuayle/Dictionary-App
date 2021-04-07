import json
from difflib import SequenceMatcher
from difflib import get_close_matches
data = json.load(open("data.json"))
word = " "
print("Welcome to the dictionary. Enter 'xx' if you wish to exit")
while word!= "xx":
    word = input("Enter a word: ")
    if word in data:
        print(data[word])
    elif word.lower() in data:
        print(data[word.lower()])
    elif word.upper() in data:
        print(data[word.upper()])
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Y/N " % get_close_matches(word, data.keys())[0])
        if yn == "Y":
            print(data[get_close_matches(word, data.keys())[0]])
        elif yn == "N":
            print("This word was not found check for errors and try again.")
        else:
            print("Response not understood.")
    elif word == 'xx':
        break
    else:
        print("This word was not found check for errors and try again.")
print("Thank you for using my dictionary.")
# word = input("Enter a word: ").lower()
# print(data[word])
