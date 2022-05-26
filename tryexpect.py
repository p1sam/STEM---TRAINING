try :
    div = 10/0
    value = int(input("Enter a number: "))
    print(value)

except ValueError:
    print("Invalid number entered")

except ZeroDivisionError:
    print("Divided by zero")