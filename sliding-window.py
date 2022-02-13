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
    indexStart, temp = 0, 0
    for indexEnd, num in enumerate(nums):
        temp += num

        #when reach to the window limit k+1
        if indexEnd-indexStart > (k-1):
            #add the average into the result array
            result.append((temp-num)/k)
            #drop the first one, take k element forward
            temp -= nums[indexStart]
            #reset the window's starting index by incrementing 1
            indexStart += 1
    # append the average of nums[-k:]
    result.append(temp/k)
    return result


def main():
    arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
    print(get_avg_of_subarrays_bf(5,arr))
    print(get_avg_of_subarrays_sw(5,arr))

main()