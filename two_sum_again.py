class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            amount = target - nums[i]
            if amount in map:
                return [map[amount], i]  # map value already there
            map[nums[i]] = i
