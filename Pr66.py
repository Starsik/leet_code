class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        x = map(str, digits)
        x = ''.join(x)
        x = int(x)
        x += 1
        res = [int(i) for i in str(x)]
        return res


if __name__ == "__main__":
    question = [1,2,3]
    answer = Solution()
    print(answer.plusOne(question))
    question = [4,3,2,1]
    print(answer.plusOne(question))
    question = [9]
    print(answer.plusOne(question))
