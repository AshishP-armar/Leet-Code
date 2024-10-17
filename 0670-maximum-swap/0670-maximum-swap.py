class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        last = {int(d): i for i, d in enumerate(digits)}
        
        for i, d in enumerate(digits):
            for larger_digit in range(9, int(d), -1):
                if last.get(larger_digit, -1) > i:
        
                    digits[i], digits[last[larger_digit]] = digits[last[larger_digit]], digits[i]
                    return int(''.join(digits))
        

        return num
