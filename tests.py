random_word = 'ana'
palabra = []
for letra in random_word:
    palabra.append(letra)
print(palabra)



print(palabra.find('a'))

""" print(random_word.count('a')) """

is_letter = random_word.count('a')


longitud = len(random_word)


print('_ '*longitud)

if(is_letter):
    pass

""" ______________________________________________________________________________ """

random_word = 'ana'
palabra = []
for letra in random_word:
    palabra.append(letra)
print(palabra)


def lienarSearch(palabra,listLen,letter):
    acertions = []
    for i in range(0,listLen):
        if(palabra[i] == letter):
            acertions.append(i)
    return acertions

letter = 'a'
listLen = len(palabra)
result = lienarSearch(palabra,listLen,letter)

if(result):
    print("Element found at index: ",result)
else:
    print("Not found")
