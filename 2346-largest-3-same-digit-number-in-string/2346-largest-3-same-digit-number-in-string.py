class Solution:
    def largestGoodInteger(self, num: str):
        valid_Num = []
        for i in range(len(num) - 2):
            sub = num[i:i+3]
            if sub[0] == sub[1] == sub[2]:
                valid_Num.append(sub)
        if not valid_Num:
            return ""
        return max(valid_Num)
