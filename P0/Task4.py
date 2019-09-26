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


telemarketers = re.compile('140[0-9]{7}')
telemarketer_callers = [x for x in calls if telemarketers.match(x[0])]


all_outgoing_calls = [x[0] for x in calls]
all_receiving_calls = [x[1] for x in calls]
all_text_senders = [x[0] for x in texts]


combined_lists = list(set(all_receiving_calls)) + list(set(all_text_senders))


suspected_telemarketers = sorted([x for x in list(set(all_outgoing_calls)) if x not in combined_lists])


print("These numbers could be telemarketers:")
for number in suspected_telemarketers:
    print(number)



# O(n) all_outgoing_calls
# O(n) all_receiving_calls
# O(n) all_text_senders
# O(2n + 2n) combined_lists
# O(3n + n log n) suspected_telemarketers

# O = (10n + n log n)














"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

