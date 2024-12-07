from typing import List

# Any number can be missing
# https://leetcode.com/problems/missing-number/description/
# Time Complexity of my Solution: https://i.imgur.com/ejkMIIY.png

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_for_loop = -1
        nums = sorted(nums)
        for num in nums:
            num_for_loop += 1
            if num_for_loop == num:
                if num_for_loop == nums[-1]:
                    return num + 1
                continue
            elif num_for_loop != num:
                missing_num = num - 1
                return missing_num

li = [9,6,4,2,3,5,7,0,1]
sol = Solution()
result = sol.missingNumber(li)
print(result)

# These are some more cases we can check this against:
'''
[0,1]
[3,0,1]
[0, 1, 3, 4, 5, 7, 9, 10, 11]
'''



