entry = input("user input> ")
output_int = ""

for ch in entry:
    if ch in "1234567890":
        output_int += ch

val = int(output_int)
print(val)
