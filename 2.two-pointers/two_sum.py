# The array is sorted
# # Two sum problem

# brute force with Time complexity O(N*LogN):
#       iterate every elements and binary search the second element
def two_sum_bf(target, nums):
    # corner case ignore for now
    for index, num1 in enumerate(nums):
        num2 = target - num1

        # Binary search num2's index        
        left = index+1
        right = len(nums)-1
        num2_index = -1
        while left<=right:
            mid = (right-left)/2+left # Update mid
            if num2 == nums[mid]:
                num2_index = mid
                break
            elif num2 > nums[mid]:
                left += 1
            elif num2 < nums[mid]:
                right -= 1
        
        if num2_index != -1: # Found num2 when num2_index is not -1
            return [index, num2_index]
    return [-1, -1]

# Imp 1: two pointers
def two_sum_tp(target, nums):
    '''Two pointers at start and end'''
    leftPointer, rightPointer = 0, len(nums)-1
    while leftPointer < rightPointer:
        currentSum = nums[leftPointer] + nums[rightPointer]
        if target == currentSum: # Found the pair
            return [leftPointer, rightPointer]
        elif target > currentSum:
            rightPointer -= 1
        else:
            leftPointer += 1
    return [-1, -1] # Not found

# Imp 2: hash table
def two_sum_ht(target, nums):
    '''Hash table'''
    numsTable = {}
    for index, num in enumerate(nums):
        if num in numsTable:
            return [numsTable[num], index]
        else:
            numsTable[target-num] = index
    
    return [-1, -1] # Not found






