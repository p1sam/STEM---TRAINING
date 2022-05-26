trial = True

while trial:
    commands = str(input("operation> "))
    if commands.lower() == "done":
        print("turning of calculator")
        trial = False
        break
    try:
        val1 = int(input("input your first number> "))
        val2 = int(input("input your second number> "))
    except ValueError:
        print("Wrong value entered")
        break
    

    if commands.lower() == "add" or "+":
        print(val1 + val2)

    elif commands.lower() == "multiply" or "*":
        print(val1 * val2)

    elif commands.lower() == "divide" or "/":
        print(val1/val2)

    elif commands.lower() == "subtract" or "-":
        print(val1 - val2)

 

    else :
        print("Command not recognised")
        print("try 'add', 'subtract', 'divide' or 'multiply'")
        print("input done if you are finished")