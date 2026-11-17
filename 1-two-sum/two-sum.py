class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dict = {}
        for idx, num in enumerate(nums):
            if target - num in dict:
                return[dict[target-num], idx]
            dict[num]=idx
        return