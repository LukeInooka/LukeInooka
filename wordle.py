def wordle(green, yellow, grey):
    from wordlist import wordlist
    words = wordlist()
    l1 = []
    l2 = []
    l3 = []
    for word in words:
        grey_count = 0
        for letter in grey:
            if letter not in word:
                grey_count += 1
            if grey_count == len(grey):
                l1.append(word)
    if len(yellow) != 0 and len(green) != 0:
        for word in l1:
            yellow_count = 0
            for letter in yellow:
                if letter[0] in word and word[int(letter[1])] != letter[0]:
                    yellow_count += 1
                if yellow_count == len(yellow):
                    l2.append(word)
        for word in l2:
            green_count = 0
            for letter in green:
                if word[int(letter[1])] == letter[0]:
                    green_count += 1
            if green_count == len(green):
                l3.append(word)
        print(l3)
    if len(yellow) == 0 and len(green) == 0:
        print(l1)
    if len(yellow) == 0 and len(green) != 0:
        for word in l1:
            green_count = 0
            for letter in green:
                if word[letter[1]] == letter[0]:
                    green_count += 1
            if green_count == len(green):
                l2.append(word)
        print(l2)
    if len(yellow) != 0 and len(green) == 0:
        for word in l1:
            yellow_count = 0
            for letter in yellow:
                if letter[0] in word and word[int(letter[1])] != letter[0]:
                    yellow_count += 1
                if yellow_count == len(yellow):
                    l2.append(word)
        print(l2)


greens = []
yellows = []
greys = []
for i in range(100):
    green_input = input('Greens(a1 b2 c3): ')
    if len(green_input) > 1:
        green_input = list(green_input.split(' '))
        for obj in green_input:
            greens.append([obj[0], obj[1]])
    yellow_input = input('yellows(a1 b2 c3): ')
    if len(yellow_input) > 1:
        yellow_input = list(yellow_input.split(' '))
        for obj in yellow_input:
            yellows.append([obj[0], obj[1]])
    grey_input = input('greys(a b c): ')
    if len(grey_input) > 1:
        grey_input = list(grey_input.split(' '))
        for obj in grey_input:
            greys.append(obj[0])
    print(wordle(greens, yellows, greys))

#%%
