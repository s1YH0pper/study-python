class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        stack = []
        nums_i = 0
        while nums_i < len(nums):
            if nums[nums_i] in stack:
                nums.pop(nums_i)
                continue
            else:
                stack.append(nums[nums_i])
            nums_i += 1
        return len(nums)
