--Task 0--
Task 0 simply requires slicing an array of arrays and getting an item in an array three times.  


       Slicing in Python is in O(k) time where K is the size of the slice. Our slices are only of size 1. So each slice is 
       only in O(1) time.
       
       Each slice is looped through to get the items. Get Item in an Array is O(1) time.
       
       Time complexity is O(1) for slice and O(3)/O(4) for the formatting.
       Worst Case: O(1)


--Task 1--
Task 1 primarily consists of 4 loops nested in 2 list comprehensions. We can simplify this by noting that looping
within a loop would be N^2 for each list comprehension. 

    Two loops of two loops = O(2n^2)
    
We then have to produce a set of the results of concatenation the two lists. I'm not sure what the time complexity of
Set() is, but since we are passing in a list I will just assume it is linear, O(N).

    Two Loops of loops + Set() = O(2n^2) + M where M is the size of the contatenated array.
    
    Worst Case is O(2n^2)
    
    


--Task 2--

There are a number of steps involved in Task 2. First we loop through the calls list, in each iteration we slice the first
two elements and loop through the slice. This is still a loop within a loop so we can say 

    call_numbers = O(n^2)
    
We then loop through our new array and create a set and produce dict of each number with a value of 0. Assuming this process
is O(N) since we have to loop through a list. 

    numbers_dict = O(n)
    
We then loop through our call numbers dict and for each entry we loop through the calls list and add a +1 to each entry in our dict.
This involves a few steps.

    1) Convert dict to list = O(N)
    2) Loop through it. = O(N)
    3) For each in that loop loop through calls = O(N)
    4) For each in the calls list we check if item exists. This is also a loop "if item in array". = O(N)
    
    Thats one indepentent loop and then three nested loops. For this section we can say O(N^3) + N
    This is a pretty inefficient. 

Finally we find the largest entry in our numbers_dict dict by calling max. This is O(N)

    Worst Case is (N^3 + N^2 + 3N). This is pretty bad and explains why the code runs really slow. 




--Task 3--

Again, there are quite a few steps for task 3.

First we compile 4 regular expressions. I'm assuming these are O(1), so we can ignore them.

Second we generate a list of all bangalore callers, which is just a loop and regex match. Ignoring the match.

    bangalore_callers = O(N) where N is length of calls list.
    
Third we concat two list comprehensions each containing a loop to get all the area codes:

    area_codes = (2N)
    
Forth we make a list of all the calls to bangalore numbers. This is a loop:

    called_to_bangalore = O(N)
    
Fifth, we take the all the area codes of bangalore callers and do 3 things:

    Set(): O(N)
    Sort(): O(n Log n)
    List(): O(N)
    Total = O(n Log n + 2n)

Finally we loop through all the unique area codes and pring them:

    O(N)
    
    Worst Case: O(n Log n +7n)


--Task 4--

Again, there are quite a few steps for task 4.

First we compile 4 regular expressions. I'm assuming these are O(1), so we can ignore them.

Second we generate a list of telemarketer_callers which is a loop:

    telemarketer_callers = O(N)
    
Third, we isolate outgoing calls, incomming calls and texts into their own lists:

    all_outgoing_calls = O(N)
    all_receiving_calls = O(N)
    all_text_senders = O(N)

Fourth we create a single list of all the calls:

    2x call Set() = O(2n)
    2x call list() = O(2n)
    
Fifth, we use a fairly complex list comprehension to create the suspected telemarketers list:

    sort() all_outgoing_calls = O(n Log n)
    list() that = O(n)
    ---
    loop through that list and for each in that list check if each in combined_lists = O(N^2)
    
Finally, loop through the suspected_telemarketers list and print them:

    O(N)
    
    Worse Case: 9n + n^2 + n Log n
    
      
    
    