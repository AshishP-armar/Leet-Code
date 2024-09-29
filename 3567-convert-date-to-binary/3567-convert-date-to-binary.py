class Solution:
    def convertDateToBinary(self, date: str) -> str:
        year = bin(int(date.split("-")[0]))[2:]
        # print(date.split("-")[1])
        month = bin(int(date.split("-")[1]))[2:]

        day = bin(int(date.split("-")[2]))[2:]


        return f"{year}-{month}-{day}"


        