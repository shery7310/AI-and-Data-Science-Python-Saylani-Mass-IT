"""
1 2 3 4 5 6 7 8 9 10
2 4 6 8 10 12 14 16 18 20
3 6 9 12 15 18 21 24 27 30
4 8 12 16 20 24 28 32 36 40
5 10 15 20 25 30 35 40 45 50
6 12 18 24 30 36 42 48 54 60
7 14 21 28 35 42 49 56 63 70
8 16 24 32 40 48 56 64 72 80
9 18 27 36 45 54 63 72 81 90
10 20 30 40 50 60 70 80 90 100

10 numbers in each row starting
Each Row starts from 1 more than previous one in the col
"""
count = 1
for row in range(1, 11): # will run loop 10 times, representing 10 rows
    for col in range(1, 11): # this means run loop 10 time for each iteration of outer loop
        print(col * count, end=" ") # count = 1 at start, col = 1 2 3 4 5 6 7 8 9 10 for each iteration
                                    # whereas count keeps increasing
                                    # for example in 2nd iteration count = 2, so each col value i.e. 1 2 3 ... is multiplied by 2
                                    # at 3rd iteration each col value is multiplied by 3
    print()
    count += 1