# this is for word list only
with open('wordlist.txt') as file:
    words = file.read()
long_lis = []
words = words.splitlines()
for word in words:
    if len(word) ==5:
        long_lis.append(word)


def wordlist():
    return long_lis

