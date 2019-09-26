"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

# Regular Expressions
fixed_line = re.compile('\(\d+\)\d+')
fixed_line_area_code = re.compile("\(\d+\)")
bangalore_numbers = re.compile('\(080\)\d+')
mobile_number = re.compile('[0-9]{5}\s[0-9]{5}')

# Lists and loops
bangalore_callers = [x for x in calls if bangalore_numbers.match(x[0])] # get a list of all the bangalore callers

area_codes = [x[1][:4] for x in bangalore_callers if mobile_number.match(x[1])] + \
             [fixed_line_area_code.match(x[1]).group(0)[1:-1] for x in bangalore_callers if fixed_line.match(x[1])] # get
# a list of both fixed line and mobile area codes


called_to_bangalore = [x for x in bangalore_callers if bangalore_numbers.match(x[1])]


# List Actions
unique_area_codes = list(sorted(set(area_codes)))
print(set(area_codes))
print(sorted(set(area_codes)))
print(unique_area_codes)



call_percent = len(called_to_bangalore) / len(bangalore_callers) * 100


# Output
print("The numbers called by people in Bangalore have codes:")
for code in unique_area_codes:
    print(code)
print("\n")
print("{0:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore".format(call_percent))





# asssumes regex.match with compiled regex is O(n)
# O(2n) bangalore_callers
# O(7n) area_codes
# O(2n) called_to_bangalore
# O(n + N Log N + n) unique_area_codes
# O(1 + 1 + 1) call_percent


# O = (13n + n Log n + 3)



"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
