
with open('text.txt', 'r') as file:
    for line in file.readlines():
        for word in line.split():
            print(word)


