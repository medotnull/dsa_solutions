def maxSubArray(self, nums: List[int]) -> int:
    cs = nums[0]
    total = nums[0]
    for i in range(1, len(nums)):
        cs = max(nums[i], cs + nums[i])
        total = max(total, cs)
    return total