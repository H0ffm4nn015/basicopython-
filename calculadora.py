
output = 0
num1 = ""
operation = ""
num2 = ""

num1 = input("Primeiro numero:\n")
operation = input("Operation (+, -, *, /)?\n")
num2 = input("segundo numero?\n")


floatnum1 = float(num1)
floatnum2 = float(num2)


if operation == "+":
    output=floatnum1+floatnum2
if operation == "-":
    output=floatnum1-floatnum2
if operation == "*":
    output=floatnum1*floatnum2
if operation == "/":
    output=floatnum1/floatnum2
if operation == "+" or operation == "-" or operation == "/" or operation == "*":
    print("resposta: "+str(output))

else:
    print("Operacao invalida") 