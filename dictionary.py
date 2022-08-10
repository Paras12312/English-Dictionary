import json
from difflib import get_close_matches

#loading data from jasn file
data=json.load(open("dictionary.json"))

#function
def translate(w):
    #code to convert into lower case
    w=w.lower()

    #to check if input is in the json file
    if w in data:
        return data[w]
        #if not getting
    elif len(get_close_matches(w,data.keys()))>0:
        yn=input("Did you mean % s instead?enter Y if yes and N if no:"%get_close_matches(w,data.keys())[0])
        yn = yn.lower()
        if yn=="y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn=="n":
            return "The word doesn't exit. Please check it again."
        else:
            return "We didn't understand . Please type again."
    else:
        return "The word doesn't exist . Please check it again."
#taking input
word=input("Please enter here:-")
output=translate(word)

if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)

input("Press ENTER to exit")
