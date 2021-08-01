from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]] 

solution = Solution()
nums: List[int] = [-3,4,3,90]
target: int = 0
result: List[int] = solution.twoSum(nums, target)
print("Result: ")
print(result)
