def dnfAlgo(nums):
    n = len(nums)
    low = 0
    mid = 0
    high = n - 1

    while mid<= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low +=1
            mid +=1

        elif nums[mid] == 1:
            mid +=1
        
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -=1

    return nums

givenNums = [2,0,1,2,1,0]
print(dnfAlgo(givenNums))