def print_num(n):
    for i in range(n):
        if i%3 == 0 and not i%5 == 0:
            print(f'foo> {i}')

        if i%5 == 0 and not i%3 ==0:
            print(f'bar> {i}')

        if i%3 == 0 and i%5==0:
            print(f'foobar> {i}')

        else:
            print(i, " not divisible")


print_num(25)
