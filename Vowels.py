def isVowels(word):
	count=0
	for ch in word:
		if ch in "aeiou":
			count=count+1
	return count
print(isVowels("hello"))
print(isVowels("Hi"))
print(isVowels("sky"))
