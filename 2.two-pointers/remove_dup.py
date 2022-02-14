'''
See Leetcode: https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/
'''


from typing import List

# My code
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # bugFix: return value is length not the array
        # if len(nums) == 1:
        #     return len(nums)
        pointer1, pointer2 = 0, 1
        while pointer2<len(nums):
            if nums[pointer1] == nums[pointer2]:
                pointer2 += 1
            else:
                nums[pointer1+1] = nums[pointer2]
                pointer1 += 1
                
        return pointer1+1

# Imp with less code from the answer
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        countLen, pointer1, pointer2 = 1, 0, 0 # 1<=len(nums)
        while pointer2 < len(nums):
            if nums[pointer1] != nums[pointer2]:
                countLen += 1
                nums[pointer1+1] = nums[pointer2]
                pointer1 += 1
            pointer2 += 1
        return countLen