"""
Can also use a set
"""

def hasDuplicate(self, nums: List[int]) -> bool:
  map = {}
  for n in nums:
    if n in map:
      return True
    map[n] = map.get(n, 0) + 1
  return False         
