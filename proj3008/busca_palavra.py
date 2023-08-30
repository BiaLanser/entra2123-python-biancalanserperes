import random_word

r = random_word.RandomWords()

while True:
    palavra = r.get_random_word()

    if (len(palavra)) > 8:
        print(palavra)
        break
    else:
        continue