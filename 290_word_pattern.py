# https://leetcode.com/problems/word-pattern/description/

"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.
"""

# test cases
"""
Example 1:

Input: pattern = "abba", s = "dog cat cat dog"

Output: true

Explanation:

The bijection can be established as:

'a' maps to "dog".
'b' maps to "cat".
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"

Output: false

Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"

Output: false
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words_arr = s.split()
        if len(pattern)!=len(words_arr):
            return False
            
        temp = {}
        for i in range(len(pattern)):
            if pattern[i] not in temp:
                temp[pattern[i]]=words_arr[i]

            else:
                if temp[pattern[i]]!=words_arr[i]:
                    return False

        temp_value = set()
        for key,value in temp.items():
            if value not in temp_value:
                temp_value.add(value)
            else:
                return False

        return True
        

