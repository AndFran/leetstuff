"""
Given a sentence and some letters
determine if you can make the sentence from the letters

"""

letters = "henewasthreetherandt"

sentence = "aandthenthree"

map = {}
for l in letters:
    map[l] = map.get(l, 0)+1

print(map)

for l in sentence:
    if l in map:
        map[l] -= 1
        if map[l] < 0:
            print("Not possible")
            break

print(map)

# O(n) and space O(n)
