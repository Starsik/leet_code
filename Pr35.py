class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for i in nums:
            if i == target:
                return nums.index(i)
            elif i > target:
                x = nums.index(i)
                return x
            elif target > max(nums):
                x = nums[-1]
                y = nums.index(x)
                y += 1
                return y
            else:
                continue


if __name__ == "__main__":
    answer = Solution()
    question = [1,3,4,5,6]
    target = 7
    print(answer.searchInsert(question, target))
