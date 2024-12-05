"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

for row in range(1, 6): # row = 1 in first iteration
    for col in range(1, row + 1): # col = 1 in first iteration
        print(col, end=" ") # 1 is printed and internal loop runs the number of row for example
                            # if col = 2 the printing starts from 1 then goes to 2
                            # if col = 3 the printing starts from 1 then goes to 2 then goes to 3
                            # this keeps happening until row reaches 6 and outer loop terminates
    print()                 # this print() runs after a set of iterations of inner loop complete

