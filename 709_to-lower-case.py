"""
https://leetcode.com/problems/to-lower-case/description/

Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

 
Example 1:

Input: s = "Hello"
Output: "hello"
Example 2:

Input: s = "here"
Output: "here"
Example 3:

Input: s = "LOVELY"
Output: "lovely"

"""

# solution first
class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()
        

# Second Way To Solve 
class Solution:
    def toLowerCase(self, s: str) -> str:


        # use ASCII numbers
        res = ""
        for c in s:
            if c.isalpha():
                value = ord(c) - ord('A')
                
                if value < 26:
                    res += chr(value + ord('a'))
                else:
                    res += c
            else:
                res += c

        return res
