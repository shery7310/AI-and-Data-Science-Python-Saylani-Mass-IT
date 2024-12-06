"""
        *
      * *
    * * *
  * * * *
* * * * *
"""


rows = 5 # number of rows
k = 2 * rows - 2 # at row 5 it's 10 - 2 which is 8
for row in range(0, rows):
    for space in range(k):
        # this will print " " 8 times for first iteration
        print(end=" ")
    k = k - 2 # after first iteration k = 6, after second k = 4 and so on
    for sym in range(row + 1): # in first iteration this will run as 1 time, then 2 time, then 3 time and so on
        print("* ", end="") # first time it will print *, then second time it will print * * and so on
    print() # after loop runs like this 1 time, 2 times, 3 times, 4 times and 5 times after each run
            # we need the pointer to go to next line so we use print() in outer main loop
