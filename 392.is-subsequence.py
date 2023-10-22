# Category: algorithms
# Level: Easy
# Percent: 47.254234%


# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
#
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
#
#  
# Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:
# Input: s = "axc", t = "ahbgdc"
# Output: false
#
#  
# Constraints:
#
#
# 	0 <= s.length <= 100
# 	0 <= t.length <= 10⁴
# 	s and t consist only of lowercase English letters.
#
#
#  
# Follow up: Suppose there are lots of incoming s, say s₁, s₂, ..., sk where k >= 10⁹, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?


# Start Code Section ----------------------------------------------------------
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sectionStart = 0
        for c in s:
            sectionStart = t.find(c, sectionStart)+1
            if sectionStart == 0:
                return False
        return True

# End Code Section ------------------------------------------------------------
