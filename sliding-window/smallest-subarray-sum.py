'''Given an array of positive numbers and a positive number ‘S,’ find the length of the smallest contiguous subarray 
whose sum is greater than or equal to ‘S’. Return 0 if no such subarray exists.'''

def smallest_subarray_sum(target,nums):
    # corner case
    if sum(nums)<target:
        return -1
    
    # space complexity: O(1)
    windowLen, windowSum = len(nums), 0
    indexStart = 0
    
    # time complexity: O(N+N) = O(N)
    for indexEnd, num in enumerate(nums):
        windowSum += num
        # shorten the window interval    
        while windowSum >= target:
            windowLen = min(windowLen, indexEnd-indexStart+1)
            windowSum-= nums[indexStart]
            indexStart += 1

    return windowLen

def smallest_subarray_sum_2p(target,nums):
    indexStart, indexEnd = 0, len(nums)-1


def main():
    arrs = [[2, 1, 5, 2, 3, 2],[2, 1, 5, 2, 8]]
    target = 7
    for nums in arrs:
        print(smallest_subarray_sum(target,nums))

main()