class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)[2:]
        temp = ""

        for n in binary:
            if n=="1":
                temp+="0"
            else:
                temp+="1"
        print(temp)
        return int(temp,2)
    