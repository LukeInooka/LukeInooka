import time, random
letters = 'abcdefghijklmnopqrstuvwxyz123456789'
print(' '.join([letters[random.randint(0, 34)] for letter in range(15)]))
a,b = time.time(),input()
print(time.time()-a)
