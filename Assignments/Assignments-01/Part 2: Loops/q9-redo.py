# Write a program to print the first 10 Fibonacci numbers.
# 1 1 2 3 5 8 13 21 34 55

# In this approach we are swapping two values with one and another

num1 = 0
num2 = 1

num = 0

while num < 9:
    num3 = num1 + num2
    print(num3, end=" ")
    if num == 0:
        print(num3, end=" ")
    num1 = num2
    num2 = num3
    num += 1