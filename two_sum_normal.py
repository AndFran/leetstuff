"""

We do:

if target - num 
  is in the map, then we have the other side of the sum 
  if its not in the map, then we add num

"""


nums = [2, 1, 5, 3]
target = 4

nums = [2, 7, 11, 15]
target = 9 


map = {}
for i, num in enumerate(nums):
    result = target - num
    if result not in map:
        map[num] = i
    else:
        print("found", map[result], "and", i)


print(map)
