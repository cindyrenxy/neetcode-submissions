class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nondup = list(set(nums))
        return len(nondup) != len(nums)