# making a simple calculator using if elif ladder 
print("1-Addition")
print("2-Subtraction")
print("3-Multiplication")
print("4-Division")
operation=int(input("Choose your operation:"))
num1=float(input("Enter your first number:"))
num2=float(input("Enter your second number:"))

if (operation in [1,2,3,4]):
    
    if(operation == 1):
        result=num1+num2
    
    elif(operation == 2):
        result=num1-num2
    
    elif(operation == 3):
        result=num1*num2
    
    elif(operation == 4):
        if(num2 != 0):
            result=num1/num2
        else:
            print("Can not divide by 0")
else:
    print("Invalid Operation!")
print("The result of your operation is {}".format(result))