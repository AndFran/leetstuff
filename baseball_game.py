"""

You are given a list of strings operations,
 where operations[i] is the ith operation you must apply
  to the record and is one of the following:

An integer x.
Record a new score of x.
'+'.
Record a new score that is the sum of the previous two scores.
'D'.
Record a new score that is the double of the previous score.
'C'.
Invalidate the previous score, removing it from the record.

Return the sum of all the scores on the record after applying all the operations.

"""
ops = ["1","C"]
record = []

for op in ops:
    if op == "+":
        record.append(record[-1]+record[-2])
    elif op == "D":
        record.append(record[-1] * 2)
    elif op == "C":
        record.pop()
    else:
        record.append(int(op))

print(record)
print("sum", sum(record))



