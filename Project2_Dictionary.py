
# Import jason data

import json
var= json.load(open('dictionary_Data.json'))

# Main function
def search(word):

    word= word.lower()

    if word in var:
        return var[word]
    elif word.title() in var:
        return var[word.title()]
    elif word.upper() in var:
        return var[word.upper()]
    else:
        print("This word does not exist. Please check again.")



# Function calling
word= input("Enter the word you want to search:")
output= search(word)
print(output)
print(type(output))