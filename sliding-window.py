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
def get_avg_of_subarrays(k, nums):
    result = []

def main():
    arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
    print(get_avg_of_subarrays_bf(5,arr))

main()