class Solution:
    def averageValue(self, nums: List[int]) -> int:
        stack = []
        for i in nums:
            if i % 3 == 0 and i % 2 == 0:
                stack.append(i)
        sum = 0
        for _ in stack:
            sum += _
        if sum:
            return sum // len(stack)
        else:
            return sum
