string = "Sample string"
length = len(string)
i = 0

for letter in string:
    if i < length:
        if letter == ' ':
            continue
        print(letter)

    i += 1
