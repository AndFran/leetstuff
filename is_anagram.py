"""
Given two strings s and t, return true if the
two strings are anagrams of each other, otherwise return false.

n anagram is a string that contains the exact same characters
as another string, but the order of the characters can be different.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_s = {}
        map_t = {}
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            map_s[s[i]] = map_s.get(s[i], 0) + 1
            map_t[t[i]] = map_t.get(t[i], 0) + 1

        return map_s == map_t
