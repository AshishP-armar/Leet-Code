class Solution:
    def countKeyChanges(self, s: str) -> int:
        if not s:
            return 0
        
        key_changes = 0
        previous_char = s[0].lower()  
        
        for i in range(1, len(s)):
            current_char = s[i].lower()  
            if current_char != previous_char:
                key_changes += 1  
                previous_char = current_char  

        return key_changes
