"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


call_numbers = [n for call in calls for n in call[0:2]]
print(call_numbers)

numbers_dict = dict.fromkeys(call_numbers, 0) # for counting
print(numbers_dict)

for number in numbers_dict.keys(): # returns list of all the keys in numbers dict
    for entry in calls: # for each key in the dict we loop through all the calls
        if number in entry: # for each call record we check if the number is in the list
            numbers_dict[number] += int(entry[3])


highest_number = max(numbers_dict, key=numbers_dict.get)

print("{} spent the longest time, {} seconds, on the phone during September 16th".format(highest_number, numbers_dict[highest_number]))



# call_numbers = O(n^2)
# numbers_dict = O(n) ?
# loop = O(n^2 + 2) double loops + dict lookup and addition
#highest_number = O(n)
# O(2n2+2n+2)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

