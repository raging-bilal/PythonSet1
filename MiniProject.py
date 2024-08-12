#Lets build a Calculator!

num1=int(input("Enter the first number: "))

op=input("Enter the operator to be performed: + , - , * , / , % , // , **:         ")

num2=int(input("Enter the second number: "))

if op=="+":
    print(num1 + num2)

elif op=="-":
    print(num1 - num2)

elif op=="*":
    print(num1 * num2)

elif op=="/":
    print(num1 / num2)

elif op=="%":
    print(num1 % num2)

elif op=="//":
    print(num1 // num2)

elif op=="**":
    print(num1 ** num2)

else:
    print("Invalid Operator! Cannot be Executed...")