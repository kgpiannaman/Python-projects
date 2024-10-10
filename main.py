# This is a sample Python script.
import string
#Read .txt file
# with open('textfile.txt', 'r', encoding='latin-1') as file:
#     content = file.read()
#     content = content.lower()

#Read json file
import json

# Open the JSON file with the correct encoding
with open('textfile.json', 'r', encoding='utf-16') as file:
 content = str(json.load(file))
# #Initializing dictionary
count_letter = {}

 #Finding number of occurences of 'l' in the content
for letter in string.ascii_lowercase:
    letter_count = content.count(letter)
    count_letter[letter] = letter_count
sorted_dict = dict(sorted(count_letter.items(),key=lambda item: item[1], reverse=True))
print(sorted_dict)






