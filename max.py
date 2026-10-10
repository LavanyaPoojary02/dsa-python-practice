def isMax(nums):
	biggest=nums[0]
	for num in nums:
		if num>biggest:
			biggest=num
	return biggest
	
print(isMax([3,2,6,1]))
