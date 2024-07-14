"""
Given an integer array nums of length n
you want to create an array ans of length 2n

Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
[nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]

Input: nums = [1,3,2,1]
Output: [1,3,2,1,1,3,2,1]

"""

nums = [1, 3, 2, 1]

# short way
nums.extend(nums)
print(nums)

print("----generic solution any amount of times----")

nums = [1, 3, 2, 1]
times = 2
length = len(nums)
destination = [0 * length for _ in range(length * times)]  # fake reserving space

for i in range(len(destination)):
    original = i % length
    destination[i] = nums[original]

print(destination)


print("------- with for loops---------")

nums = [1, 3, 2, 1]
destination = []
times = 2 

for _ in range(times):
    for i in range(len(nums)):
        destination.append(nums[i])

print("dest", destination)
