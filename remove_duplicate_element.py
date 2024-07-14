"""

Given an integer array nums and an integer val,
 remove all occurrences of val in nums in-place.

The order of the elements may be changed.
 Then return the number of elements in nums which are not equal to val.

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]

"""
nums = [0,1,2,2,3,0,4,2]
val = 2
r = None
for i in range(len(nums)):
    if nums[i] == val and r is None:
        r = i
    if nums[i] != val and r is not None:
        nums[r] = nums[i]
        r += 1

print("final", nums[:r])
