#opening and editing files in python


def func(n):
    for i in range(n+1):
        if i%2==0:
            with open("results.txt", "a") as f:
                output_str = str(i) + " divided by 2 is " + str(i/2) + "\n"

                f.write(output_str)
        elif i%2!=0:
            with open("results.txt.txt", "a") as f:
                output_str= str(i) + " multiplied by 2 is " + str(i*2) + "\n"
                f.write(output_str)

        else:
            pass
    f.close()

    #with open("results.txt", "r") as r:
        #print(r.read())


func(10)

