def isAnagram(s,t):
  return sorted(s)==sorted(t)
print(isAnagram("listen","silent"))
print(isAnagram("cat","car"))
print(isAnagram("night", "thing"))

