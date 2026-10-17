#Minimum Number 

def isMin(nums):
	smallest=nums[0]
	for num in nums:
		if num<smallest:
			smallest=num
	return smallest
print(isMin([3,2,7,9,1]))
