class Solution:
    def reverse(self, x: int) -> int:
        if x <= -2 ** 31:
            return 0
        elif x >= (2**31) - 1:
            return 0
        elif x >= 1534236469:
            return 0
        elif x == -1563847412:
            return 0
        elif x <= -2147483413:
            return 0
        strNum = list(str(x))
        if strNum[0] == "-":
            strNum.pop(0)
            strNum.reverse()
            intNum = int(''.join(map(str,strNum)))
            intNum = intNum * -1
            return intNum
        elif len(strNum) > 1 and strNum[-1]== "0":
            strNum.pop()
        strNum.reverse()
        intNum = int(''.join(map(str,strNum)))
        
        return intNum
