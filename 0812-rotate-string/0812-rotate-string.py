class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # Check if the lengths of s and goal are the same
        if len(s) != len(goal):
            return False
        # Check if goal is a substring of s + s
        return goal in (s + s)
