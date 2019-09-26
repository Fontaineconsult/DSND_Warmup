"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv



with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open("calls.csv", "r") as f:
    reader = csv.reader(f)
    calls = list(reader)




call_numbers = [n for call in calls for n in call[0:2]] + [n for text in texts for n in text[0:2]]

# call_numbers (n^2 + n^2)
# O=(2n^2)


print("There are {} different telephone numbers in the records".format(len(set(call_numbers))))

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
