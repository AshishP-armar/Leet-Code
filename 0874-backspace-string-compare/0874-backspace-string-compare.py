class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.remove_space(s)==self.remove_space(t)
    
    def remove_space(self,s):
        stack = []

        for char in s:
            if char != "#":
                stack.append(char)
            else:
                if len(stack)!=0:
                    stack.pop()
        return "".join(stack)
        