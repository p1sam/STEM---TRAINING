while True:


    def replace_in(phrase):
        word = "  "
        for letter in phrase:
            if letter in "aeiou":
                word = word + "g"

            elif letter in "AEIOU":
                word = word + "G"
            else:
                word = word + letter

        return word

    print(replace_in(input("enter a phrase: ")))