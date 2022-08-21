from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        finding_num_dict = {}
        for index1, num1 in enumerate(nums):
            finding_num_dict[target - num1] = index1
        
        for index2, num2 in enumerate(nums):
            if finding_num_dict.get(num2) != None:
                if finding_num_dict.get(num2) != index2:
                    return [finding_num_dict.get(num2), index2]


sol = Solution()

ans = sol.twoSum([2,7,11,15], 9)
print(ans)