# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

if __name__ == '__main__':
    f = open("J:\Python_all\Projekty Pycharm\szyfrowanie\Tekst_do_szyfru.txt", "r", encoding="utf-8")
    z = open("J:\Python_all\Projekty Pycharm\szyfrowanie\Tekst_zmieniony.txt", "w", encoding="utf-8")
    key = 3
    read_text = f.read()
    table_with_letters = [''] * key
    trying = [''] * key
    new_text = ""
    strip_text = read_text.replace(" ", "")
    upper_text = strip_text.upper()

    for sign in upper_text:
        if sign == "A":
            signs_to_random = ['Ž', 'š', 'C']
            random_number = random.randint(0, len(signs_to_random)-1)
            sign_to_put = signs_to_random[random_number]
            new_text += sign_to_put
        elif sign == "B":
            signs_to_random = ['Ÿ', '¢', 'M']
            random_number = random.randint(0, len(signs_to_random) - 1)
            sign_to_put = signs_to_random[random_number]
            new_text += sign_to_put
        elif sign == "C":
            signs_to_random = ['¥', '§', 'R']
            random_number = random.randint(0, len(signs_to_random) - 1)
            sign_to_put = signs_to_random[random_number]
            new_text += sign_to_put
        elif sign == "D":
            signs_to_random = ['©', '®', 'F']
            random_number = random.randint(0, len(signs_to_random) - 1)
            sign_to_put = signs_to_random[random_number]
            new_text += sign_to_put
        elif sign == "E":
            signs_to_random = ['°', 'À', 'Z']
            random_number = random.randint(0, len(signs_to_random) - 1)
            sign_to_put = signs_to_random[random_number]
            new_text += sign_to_put
        elif sign == "F":
            signs_to_random = ['Æ', 'Ç', 'S']
            random_number = random.randint(0, len(signs_to_random) - 1)
            sign_to_put = signs_to_random[random_number]
            new_text += sign_to_put
        elif sign == "G":
            signs_to_random = ['Ð', 'Ø', 'L']
            random_number = random.randint(0, len(signs_to_random) - 1)
            sign_to_put = signs_to_random[random_number]
            new_text += sign_to_put
        elif sign == "H":
            signs_to_random = ['ß', 'â', 'N']
            random_number = random.randint(0, len(signs_to_random) - 1)
            sign_to_put = signs_to_random[random_number]
            new_text += sign_to_put
        elif sign == "I":
            signs_to_random = ['î', 'õ', 'D']
            random_number = random.randint(0, len(signs_to_random) - 1)
            sign_to_put = signs_to_random[random_number]
            new_text += sign_to_put
        elif sign == "J":
            signs_to_random = ['þ', 'Ď', 'G']
            random_number = random.randint(0, len(signs_to_random) - 1)
            sign_to_put = signs_to_random[random_number]
            new_text += sign_to_put
        elif sign == "K":
            signs_to_random = ['Ē', 'Ħ', 'K']
            random_number = random.randint(0, len(signs_to_random) - 1)
            sign_to_put = signs_to_random[random_number]
            new_text += sign_to_put
        elif sign == "L":
            signs_to_random = ['Ķ', 'Œ', 'O']
            random_number = random.randint(0, len(signs_to_random) - 1)
            sign_to_put = signs_to_random[random_number]
            new_text += sign_to_put
        elif sign == "M":
            signs_to_random = ['Ř', 'Ť', 'Q']
            random_number = random.randint(0, len(signs_to_random) - 1)
            sign_to_put = signs_to_random[random_number]
            new_text += sign_to_put
        elif sign == "N":
            signs_to_random = ['Ŵ', 'Ɓ', 'T']
            random_number = random.randint(0, len(signs_to_random) - 1)
            sign_to_put = signs_to_random[random_number]
            new_text += sign_to_put
        elif sign == "O":
            signs_to_random = ['Ǝ', 'Ɠ', 'P']
            random_number = random.randint(0, len(signs_to_random) - 1)
            sign_to_put = signs_to_random[random_number]
            new_text += sign_to_put
        elif sign == "P":
            signs_to_random = ['Ɯ', 'Ʀ', 'U']
            random_number = random.randint(0, len(signs_to_random) - 1)
            sign_to_put = signs_to_random[random_number]
            new_text += sign_to_put
        elif sign == "Q":
            signs_to_random = ['Ư', 'Ʒ', 'V']
            random_number = random.randint(0, len(signs_to_random) - 1)
            sign_to_put = signs_to_random[random_number]
            new_text += sign_to_put
        elif sign == "R":
            signs_to_random = ['ƹ', 'Ǣ', 'W']
            random_number = random.randint(0, len(signs_to_random) - 1)
            sign_to_put = signs_to_random[random_number]
            new_text += sign_to_put
        elif sign == "S":
            signs_to_random = ['Ǭ', 'Ƕ', 'J']
            random_number = random.randint(0, len(signs_to_random) - 1)
            sign_to_put = signs_to_random[random_number]
            new_text += sign_to_put
        elif sign == "T":
            signs_to_random = ['ȡ', 'Ȭ', 'H']
            random_number = random.randint(0, len(signs_to_random) - 1)
            sign_to_put = signs_to_random[random_number]
            new_text += sign_to_put
        elif sign == "U":
            signs_to_random = ['ȸ', 'Ⱥ', 'B']
            random_number = random.randint(0, len(signs_to_random) - 1)
            sign_to_put = signs_to_random[random_number]
            new_text += sign_to_put
        elif sign == "V":
            signs_to_random = ['Ɇ', 'Ɏ', 'E']
            random_number = random.randint(0, len(signs_to_random) - 1)
            sign_to_put = signs_to_random[random_number]
            new_text += sign_to_put
        elif sign == "W":
            signs_to_random = ['ɕ', 'ɣ', 'Y']
            random_number = random.randint(0, len(signs_to_random) - 1)
            sign_to_put = signs_to_random[random_number]
            new_text += sign_to_put
        elif sign == "X":
            signs_to_random = ['ɯ', 'ɶ', 'A']
            random_number = random.randint(0, len(signs_to_random) - 1)
            sign_to_put = signs_to_random[random_number]
            new_text += sign_to_put
        elif sign == "Y":
            signs_to_random = ['ʉ', 'ʞ', 'X']
            random_number = random.randint(0, len(signs_to_random) - 1)
            sign_to_put = signs_to_random[random_number]
            new_text += sign_to_put
        elif sign == "Z":
            signs_to_random = ['ʨ', 'ʫ', 'I']
            random_number = random.randint(0, len(signs_to_random) - 1)
            sign_to_put = signs_to_random[random_number]
            new_text += sign_to_put
        else:
            new_text += sign

    for column in range(key):
        pointer = column

        while pointer < len(new_text):
            table_with_letters[column] += new_text[pointer]
            pointer += key

    text_to_file = "".join(table_with_letters)
    z.write(text_to_file)





