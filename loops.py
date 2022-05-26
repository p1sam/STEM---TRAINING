my_list = [2, 4, 5, 3, 5, 7]
other_list = [ ]
for i in my_list:
    print(i)
    other_list.append(i)

print(other_list)
o_list = [i for i in my_list]
print(o_list)
other_list.clear()
for elem in my_list:
    if elem % 2 == 0:
        other_list.append(elem)

print(other_list)
other_list = [elem for elem in my_list if elem % 2 == 0]
print(other_list)
