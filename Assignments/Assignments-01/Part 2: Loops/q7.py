# Find the factorial of a number using a while loop.

num = int(input("Enter Any Number:\n"))

counter = 2
fact = 1
while counter < num:
    fact *= counter
    counter += 1

print(f"The factorial is: {fact*num}") 

'''
Here's how we can achieve the same thing iterating reversely i.e. 5, 4, 3, 2, 1...

factu = 1
count = num -1
while count > 1:
    factu *= count
    count -= 1  

print(f"The factorial is: {factu*num}")
Such Code must always be dry-run    
 '''


