from typing import List

# My code
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''Three pointers to find in a sorted array'''
        # No need to find the triplet when lenght is less than 3
        if len(nums) < 3:
            return []
        triplets = []
        nums.sort()
        for currentIndex in range(len(nums)-2):
            target = 0 - nums[currentIndex]
            pointer1, pointer2 = currentIndex+1, len(nums)-1
            # Alternative: write below as another function
            while pointer1<pointer2:
                currentSum = nums[pointer1] + nums[pointer2]
                if target == currentSum:
                    triplet = [nums[currentIndex], nums[pointer1], nums[pointer2]]
                    if triplet not in triplets:
                        triplets.append(triplet)
                    pointer1 += 1
                elif target >currentSum:
                    pointer1 += 1
                elif target < currentSum:
                    pointer2 -= 1
        return triplets

#Good answer
def search_triplets(arr):
  arr.sort()
  triplets = []
  for i in range(len(arr)):
    if i > 0 and arr[i] == arr[i-1]:  # skip same element to avoid duplicate triplets
      continue
    search_pair(arr, -arr[i], i+1, triplets)

  return triplets


def search_pair(arr, target_sum, left, triplets):
  right = len(arr) - 1
  while(left < right):
    current_sum = arr[left] + arr[right]
    if current_sum == target_sum:  # found the triplet
      triplets.append([-target_sum, arr[left], arr[right]])
      left += 1
      right -= 1
      while left < right and arr[left] == arr[left - 1]:
        left += 1  # skip same element to avoid duplicate triplets
      while left < right and arr[right] == arr[right + 1]:
        right -= 1  # skip same element to avoid duplicate triplets
    elif target_sum > current_sum:
      left += 1  # we need a pair with a bigger sum
    else:
      right -= 1  # we need a pair with a smaller sum

