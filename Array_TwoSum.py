from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index1, num1 in enumerate(nums):
            for index2, num2 in enumerate(nums):
                if index1 != index2:
                    if num1 + num2 == target:
                        return [index1, index2]

sol = Solution()

ans = sol.twoSum([2,7,11,15], 9)
print(ans)