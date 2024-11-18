class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        N_divisible = 0
        divisible = 0

        for num in range(1,n+1):
            if num%m==0:
                divisible+=num
            else:
                N_divisible+=num

        return N_divisible - divisible
        

    