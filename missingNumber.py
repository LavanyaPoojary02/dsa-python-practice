def missingNumber(nums):
	n=len(nums)
	expected=n*(n+1)//2
	actual = sum(nums)
	return expected-actual
print(missingNumber([3,0,1]))
print(missingNumber([1,0,3]))
