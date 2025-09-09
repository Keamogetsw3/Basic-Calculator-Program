print("Simple Calculator")
print("1 = add")
print("2 = substract")
print("3 = divide")
print("4 =  multiply")
option = int(input("choose an operation: "))

if(option in [1,2,3,4]):
    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))
    
    if(option == 1):
        result = num1+ num2
    elif(option == 2):
        result = num1 - num2
    elif(option == 3):
        result = num1 // num2
    elif(option == 4):
        result = num1 * num2
    
else:
    print("Invalid operation entered")
    
print("The results is equal to {}".format(result))
