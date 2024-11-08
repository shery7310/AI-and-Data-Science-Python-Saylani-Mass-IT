''' 0 1 1 2 3 5 8 13 21 34 55
Some People say that Fibonacci Series starts with 0 and some say it starts with 1.
We are going to start it with 1
Each Next number is the sum of previous/preceding 2 numbers
In this implementation I am using for loop to print fibonacci series
there is no need to use list but i am using it so we actually see how varaible sum is being created
in each iteration.
'''

a, b = 0, 1
fibonacci_10 = [1]
# print(f"{b}", end=" ")
for i in range(9):
    sum = a + b # a = 0 + b = 1
    print(f"(a:{a} + b:{b}) = {sum}") 
    print(sum, end=" ") # 1 2 3 5 8 13 21 34 55 would have given us entire series without list
    fibonacci_10.append(sum)
    a = b
    b = sum

print("Actual Fibonacci Series:")
for elem in fibonacci_10:
    print(elem, end=" ")
