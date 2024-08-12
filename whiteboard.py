# Running Sum of 1d Array
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.
# Example 1:
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
# Example 2:
# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]
# Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
# Example 3:
# Input: nums = [3,1,2,10,1]
# Output: [3,4,6,16,17]


nums = [1,2,3,4]
# need to return [1,3,6,10]

def running_sum(arr):
    running_sum = []
    i = 0
    if not running_sum:
        running_sum.append(arr[0])
        i += 1 
    while len(running_sum) < len(arr):
        sum = arr[i] + running_sum[i-1]
        running_sum.append(sum)
        i += 1

    return running_sum

print(running_sum(nums))

nums = [1,1,1,1,1]
print(running_sum(nums))

nums = [3,1,2,10,1]
print(running_sum(nums))