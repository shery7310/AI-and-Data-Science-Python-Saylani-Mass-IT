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

li = [0, 1]
sol = Solution()
result = sol.missingNumber(li)
print(result)