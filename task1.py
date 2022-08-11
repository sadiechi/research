num1 = 0 #human years variable
result = 0 #dog years result variable

num1 = int(input("Input a dog's age in human years: "))

if(num1>2):
    result = ((num1-2)*4)+(2*10.5)
elif(num1<=2):
    result=(num1*10.5)
else:
    print("Wrong Input")

print("The dog's age in dog's years is ", result)