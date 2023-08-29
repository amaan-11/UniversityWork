number="test"
nums=[]
while number!="":
    number=(input("Enter a number"))
    if number!="":
        nums.append(number)
nums.sort()
print(nums[0])
lowest=nums[0]
greatest=nums[len(nums)-1]
print("The greatest number = "+greatest+"\nThe lowest number = "+lowest)