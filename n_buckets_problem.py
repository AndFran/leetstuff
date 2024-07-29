"""
Buckets problem

.B..B...B   calc min moves to get B.B.B or .B.B.B etc i.e. an alternating sequence


Brute force, really, we know that a sequence must be alternating 
beginning on either an even or odd index. 
so we generate a sequence of indices of where the Bs can go and compare them with 
the starting positions 

probably to do this better would be to start the start index at the position of the first B 

"""


s = "B.BB.B..B"
s = "..B....B.BB"
s = "BB.B.BBB..."
s = "....B.B.."

bucket_pos = [i for i in range(len(s)) if s[i] == "B"]
print(bucket_pos)
print("------")
start=0
while True:
    res = []
    for i in range(start, len(s), 2):
        res.append(i)
        if len(res) == len(bucket_pos):
            print("leaving as all buckets full")
            break
    start += 1
    if len(res) < len(bucket_pos):
        print("breaking no space")
        break
    else:
        print(res)
        r = set(res)
        print("Diff is", len(r.difference(bucket_pos)))
    res = []
