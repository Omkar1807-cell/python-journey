def largest(nums):
    largest = nums[0]
    for i in nums:
        if i > largest:
            largest = i
    return largest

nums = [1,2,3,4,5,6,7,8,9]
print(largest(nums))
