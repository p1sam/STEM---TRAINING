def greater(a, b):
    for i in range(b):
        if i > a:
            print(f"{i} is greeter than {a}")

        if i == a:
            print(f"{i} is equal to {a}")

        else:
            print(f"{i} is less than {a}")

greater(25, 32)