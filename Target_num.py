def istarget(num,tgnum):
	count=0
	for nums in num:
		if nums==tgnum:
			count+=1
	return count
print(istarget([1,2,3,2,2],2)
