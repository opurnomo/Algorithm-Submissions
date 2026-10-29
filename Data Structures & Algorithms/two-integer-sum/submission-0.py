class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        H = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in H:
                return [H[diff], i]
            H[n] = i
        return None
        