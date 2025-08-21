def threeSum(nums):
  nums.sort()
  res = []
  for i in range(len(nums)):
    low = i+1
    high = len(nums) - 1
    while low != high:
      sum = nums[i] + nums[low] + nums[high]
      if sum == 0:
        res.append([nums[i], nums[low], nums[high]])
        low+=1
        high-=1