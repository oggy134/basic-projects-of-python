#Calculator using python

Operator=input("Choose the Operator + , -, *, /: ")
num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))

if Operator=="+":
    result=(num1+num2)
    print(result)
elif Operator=="-":
    result=(num1-num2)
    print(result)
elif Operator=="*":
    result=(num1*num2)
    print(result)
elif Operator=="/":
    result=(num1/num2)
    print(round(result ,3))
else:
    print(f"{Operator} is not a valid Operator")