sent =input('Write a sentence : ')

vowels =['a','e','i','o','u']

count = 0

for i in sent:
    if i in vowels:
        count += 1
if count == 1:
    print('Ther is a single vowel in the sentence.')      
elif count>1:
    print('There are', count,'vowels in the sentence.')