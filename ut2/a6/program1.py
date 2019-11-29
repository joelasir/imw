import sys

sentence = sys.argv[1]

def count_words(sentence):
    summary = {}
    sentence_as_list = sentence.split()
    for char in sentence_as_list:
        if char in summary:
            summary[char] = summary[char] + 1
        else:
            cont = 1
            summary[char] = cont

    return summary

for word, rep in (count_words(sentence)).items():
    print(word, ': ', rep)
