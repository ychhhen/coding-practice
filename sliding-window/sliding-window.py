'''
Sliding windows
'''

# Get the average of consecutive k elements in array nums

# brute force: iterating the array and append the resultult each time until len(nums)-(k-1)
def get_avg_of_subarrays_bf(k, nums):
    result = []
    for i in range(len(nums)-k+1):
        result.append(sum(nums[i:i+k])/k)
        
    return result

# Imp1: sliding window
def get_avg_of_subarrays_sw(k, nums):
    result = []
    indexStart, windowSum = 0, 0
    for indexEnd, num in enumerate(nums):
        windowSum += num
        #when reach to the window limit k
        if indexEnd-indexStart >= (k-1):
            #add the average into the result array
            result.append(windowSum/k)
            #drop the first one, take k element forward
            windowSum -= nums[indexStart]
            #reset the window's starting index by incrementing 1
            indexStart += 1

    return result


def main():
    k = 5
    arrs = [[1, 3, 2, 6, -1, 4, 1, 8, 2],[2,3,3,2]]
    for arr in arrs:
        print(get_avg_of_subarrays_bf(k,arr))
        print(get_avg_of_subarrays_sw(k,arr))

main()