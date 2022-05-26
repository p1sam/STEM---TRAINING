from tkinter import W


words = ['apples', 'love', 'people','!']
words.append("cherry")

words.remove("cherry")
print(words)
print(words.pop(1))
words_2 = ["cherry" + "tomato"]
print(words_2)
words_3 = (words + words_2)
print(words_3)
words.extend(words_2)
words_2.clear()
print(words_2)

words_4 = ("apples", "oranges", "something")
print(words_4)
print(words_4[1])


new_list = list(words_4)
new_list.append("tomatoes")
words_4 = tuple(new_list)
print(words_4)

fruits_4 = ("apple", "oranges", "oranges", "oranges")
fruits_5 = {"apple", "oranges", "oranges", "oranges"}
print(fruits_5)


"apple", "oranges", "oranges", "oranges"