"""
1 2 3 4 5 6
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""

col_num = 7 # After all inner loop iterations run
            # we need to reduce the number of times inner loop runs
for rows in range(1, 7): # outer loop represents number of rows
    for col in range(1,col_num): #inner loop represent number of columns
        print(col, end=" ") # in first iteration this runs from 1 to 6
                            # in the second it runs from 1 to 5 and then so on
    print()                 # after 6 is printed it means all internal loop iterations have
                            # successfully ran for first iteration of outer loop, so print()
                            # takes the control to the next line
    col_num -= 1            # after all inner iterations are completed for an iteration
                            # col_num is reduced so next time inner loop has to run
                            # 1 number less than the previous number of iterations


