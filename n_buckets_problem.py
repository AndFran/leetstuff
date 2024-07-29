"""
Buckets problem

.B..B...B   calc min moves to get B.B.B or .B.B.B etc i.e. an alternating sequence
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
