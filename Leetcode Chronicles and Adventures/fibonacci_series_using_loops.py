class Solution:
     def fib(self, n: int) -> int:
        a, b = 0, 1
        if n <=1:
            return n
        else:
            for _ in range(n):
                result = a + b
                a = b
                b = result
                return a

# you need to create an object and pass it an index to run it                