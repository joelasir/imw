import sys


def num_vowels(text):
    num_vowels = 0
    for char in text.lower():
        if char in 'aeiou':
            num_vowels += 1
    return num_vowels


def num_whitespaces(text):
    num_whitespaces = 0
    for char in text:
        if char in ' ':
            num_whitespaces +=1
    return num_whitespaces


def num_digits(text):
    num_digits = 0
    for num in text:
        if num in '0123456789':
            num_digits += 1
    return num_digits


def num_words(text):
    num_words = 0
    str_as_list = text.split()
    for words in str_as_list:
        num_words += 1
    return num_words


def reverse(text):
    return text[::-1]


def length(text):
    length = len(text)
    return length


def halfs(text):
    halfs = int(len(text) / 2)
    return f'{text[:halfs]} | {text[halfs:]}'


def upper_vowels(text):
    str = ""
    for char in text:
        if char in 'aeiou':
            str = str + char.upper()
        else:
            str = str + char
    return str


def sorted_by_words(text):
    str_as_list = text.split()
    list_sorted = sorted(str_as_list)
    return " ".join(list_sorted)


def length_of_words(text):
    str_as_list = text.split()
    length_of_words = []
    for words in str_as_list:
        size = str(len(words))
        length_of_words.append(size)
    return " ".join(length_of_words)


if __name__ == '__main__':
    text = sys.argv[1]
    print('Number of vowels:', num_vowels(text))
    print('Number of whitespaces:', num_whitespaces(text))
    print('Number of digits:', num_digits(text))
    print('Number of words:', num_words(text))
    print('Reverse of text:', reverse(text))
    print('Length of text:', length(text))
    print('Halfs of text:', halfs(text))
    print('Text with uppercased vowels:', upper_vowels(text))
    print('Sorted by words:', sorted_by_words(text))
    print('Length of words:', length_of_words(text))
