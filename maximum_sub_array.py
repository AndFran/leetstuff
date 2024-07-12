nums = [-2,1,-3,4,-1,2,1,-5,4]
#nums = [1]
nums = [5,4,-1,7,8]
#nums = [-10, -11, -12, -13, -14]


s = 1
result = [nums[0]]
total = nums[0]
winner = total
while s < len(nums):
    current = nums[s]
    if total + current < current:
        result.clear()
        total = 0
    result.append(current)
    total += current
    s += 1

    if total > winner:
        winner = total

print("Final winner is", winner)
