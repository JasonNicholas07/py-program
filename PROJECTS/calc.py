# py calculator program

def calc(num1, num2, op):
    if (op == '+'):
        return num1+num2
    elif (op == '-'):
        return num1-num2
    elif (op == '*' or op == 'x' or op == '.'):
        return num1*num2
    elif (op == '/'):
        if (num2 == 0):
            print("Error, Division by zero")
        else:
            return num1/num2
    elif (op == '%'):
        if (num2 == 0):
            print("Error, Mivision by zero")
        else:
            return num1%num2
    else:
        return print("Error!, operator unidentified")
    
x = float(input("Input first number: "))
op = input("Input operator: ")
y = float(input("Input second number: "))

result = calc(x, y, op)

print("")
print("Result:", result)
