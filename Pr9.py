class Solution:
    def isPalindrome(self, x: int) -> bool:
        check2 = []
        checking = list(str(x))
        for i in checking:
            check2.append(i)
        check2.reverse()


        if checking == check2:
            return True
        else:
            return False

if __name__ == "__main__":
    answer = Solution()
    question = 44
    print(answer.climbStairs(question))
