class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        while i < n - 1:
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
                i += 1
            i += 1
        new_list = [0] * n
        i = 0
        for _ in nums:
            if _:
                new_list[i] = _
                i += 1
        return new_list
