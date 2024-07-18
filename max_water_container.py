"""
You are given an integer array heights where heights[i]
represents the height of the ith bar.

You may choose any two bars to form a container.
 Return the maximum amount of water a container can store.

Input: height = [1,7,2,5,4,7,3,6]
Output: 36


We start on the right because that way we optimize x 

"""

height = [1,7,2,5,4,7,3,6]
l = 0
r = len(height)-1
current_winner = min(height[l], height[r]) * (r-l)          # min height of 2 bars * the space between the 2, r is always > l

while l < r:
    area = min(height[l], height[r]) * (r-l)
    if area > current_winner:
        current_winner = area

    if height[l] < height[r]:
        l += 1
    else:
        r -= 1


print(current_winner)
