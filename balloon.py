'''
Given a string text, you want to use the characters of text to form
as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.


Example 1:
Input: text = "nlaebolko"
Output: 1

Example 2:
Input: text = "loonbalxballpoon"
Output: 2

Example 3:
Input: text = "leetcode"
Output: 0


Constraints:

1 <= text.length <= 10^4
text consists of lower case English letters only.


build two hash maps
letter: count

for each letter and count we get the lowest value possible

mins(map[k] // target_map[k])

'''

letters = "nlaebolko"
letters = "loonbalxballpoon"
#letters = "leetcode"
target = "balloon"
map = {}
target_map = {}
for l in letters:
    map[l] = map.get(l, 0) +1

for l in target:
    target_map[l] = target_map.get(l, 0) + 1
    if l not in map:
        print("NOT POSSIBLE")

print(map)
print(target_map)


results = []
for k, v in target_map.items():
    results.append(map[k] // target_map[k])
    print(k, map[k] // target_map[k])    # want the minimum value here

print(min(results))
