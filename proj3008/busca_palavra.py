from random_word import RandomWords

while True:
    palavra = RandomWords.get_random_word()

    if (len(palavra)) == 8:
        print(palavra)
        break
    else:
        continue