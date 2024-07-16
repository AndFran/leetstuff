def alphabetSoupBuiltIns(string: str):
    letters = list(string)
    letters.sort()
    return "".join(letters)


def alphabetSoupSpaceBrute(string: str):
    # simple compare to everything O**2
    res = list(string)

    for i in range(len(res)):
        for j in range(i + 1, len(res)):
            if res[i] > res[j]:
                res[i], res[j] = res[j], res[i]
    return "".join(res)


a = alphabetSoupBuiltIns("hello")
print(a)

a = alphabetSoupSpaceBrute("abcdefga")
print(a)
