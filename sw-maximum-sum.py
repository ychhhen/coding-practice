def maximum_sum_subarray(k,nums):

    # edge case: only k elements in the array
    if len(nums) == k:
        return sum(nums)
    
    maxSum = 0
    indexStart = 0 
    windowSum = 0

    for indexEnd,num in enumerate(nums):
        windowSum += num
        if indexEnd - indexStart >= k-1:
            # update sum in each window
            maxSum = max(maxSum,windowSum)
            windowSum -= nums[indexStart]
            indexStart += 1
    return maxSum

def main():
    # ans: 9
    k = 3
    arr = [2, 1, 5, 1, 3, 2]
    print(maximum_sum_subarray(k,arr))
    # ans: 7
    k1 = 2
    arr1 = [2, 3, 4, 1, 5]
    print(maximum_sum_subarray(k1,arr1))

main()