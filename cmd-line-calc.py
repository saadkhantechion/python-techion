leftOps = int(input("Enter left operand:"))
rightOps = int(input("Enter right operand:"))
operation = input("Enter operation:")

if operation == "+":
    print("Sum = ",leftOps + rightOps)
elif operation == "-":
    print("Minus = ", leftOps - rightOps)
elif operation == "*":
    print("Multiply = ", leftOps * rightOps)
elif operation == "/":
    print("Divide = ",leftOps,"/",rightOps,"=", leftOps / rightOps)
else:
    print("Operation not supported")
