#Divisible By Five 

def divFive(nums):
    for i in range(1, nums + 1):
        if i % 5 == 0:
            print("Buzz")
        else:
            print(i)

divFive(7)
