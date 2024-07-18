"""
Given an array of integers numbers that is sorted in non-decreasing order.

Return the indices (1-indexed) of two numbers, [index1, index2],
such that they add up to a given target number target and index1 < index2.

Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

There will always be exactly one valid solution.

Your solution must use  O(1) additional space.

Input: numbers = [1,2,3,4], target = 3

Output: [1,2]

the returned indexes must be zero indexed.

if we dont need our own binary search implementation we can just use 

try:
    numbers[i:].index(to_find)
    //found here
except ValueError:
    // not found

"""


class Solution:

    def bin_search(self, numbers: list[int], to_find) -> tuple[bool, int]:
        left = 0
        right = len(numbers)-1
        print(numbers[left], numbers[right])

        while left <= right:
            mid = (left + right) // 2
            current = numbers[mid]
            if current == to_find:
                print(current, "found at index", mid)
                return True, mid
            elif current < to_find:
                left = mid + 1
            else:
                right = mid - 1


        return False, -1

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0 
        while i < len(numbers)-1:
            current = numbers[i]    
            to_find = target - current
            found = self.bin_search(numbers[i:], to_find)
            if found[0]:                
                return [i+1, i+found[1]+1]
            i += 1
