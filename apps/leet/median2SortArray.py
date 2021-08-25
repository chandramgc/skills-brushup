from typing import List


from typing import List
class Solution(object):
    def findMedianSortedArrays(self, nums1: List, nums2: List):
        nums = nums1 + nums2
        nums.sort()
        mid = len(nums) // 2
        median_value =  nums[mid] if (len(nums)%2 != 0) else ((nums[mid] + nums[mid-1])/2)
        return median_value                    

solution = Solution()
nums1 = [1, 2]
nums2 = [3, 4]

result =  solution.findMedianSortedArrays(nums1, nums2)
print("result: " + str(result))