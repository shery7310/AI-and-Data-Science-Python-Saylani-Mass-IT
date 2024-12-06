"""
   *
  ***
 *****
*******

3 spaces at start and 3 after the first star, we need to print 1 star
2 spaces at the start for 2nd row of stars, we need to print 3 stars
1 space at the start for 3rd row, we need to print 5 stars
no space in the last row, we need to print 7 stars
"""
space_count = 3 # in each row number of spaces are getting reduced that's why we need this variable
num = 0 # in each row the number of star is increasing by two from the previous one

for row in range(1, 5): # We need 4 rows so we run this 4 times
    spaces = ' ' * space_count # a new string of spaces is made each time loop restarts
    print(spaces, end="") # in the first iteration 3 spaces are added to the start of stars
                          # and then the end doesn't take the flow to the next line
                          # instead the * in next line of code will start printing from spaces
    print('*' * (row + num)) # in first iteration row = 1 and num = 0 so * is printed 1 time
                             # in the second iteration row = 2 and num = 1, 2 + 1 = 3 so 3 * are printed
    num += 1              # after each print statement value of num increases by 1
    space_count -= 1      # after each print statement value of space_count decreases by 1

