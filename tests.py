""" random_word = 'ana'
palabra = []
for letra in random_word:
    palabra.append(letra)
print(palabra)



print(palabra.find('a'))

print(random_word.count('a')) 

is_letter = random_word.count('a')


longitud = len(random_word)


print('_ '*longitud)

if(is_letter):
    pass """

""" ______________________________________________________________________________ """

game = False
progreso = ''
while(game == False):
    random_word = 'hpta'
    palabra = []
    for letra in random_word:
        palabra.append(letra)

    listLen = len(palabra)
    # print('_ '*listLen)

    def lienarSearch(palabra,listLen,letter):
        acertions = []
        for i in range(0,listLen):
            if(palabra[i] == letter):
                acertions.append(i)
            else:
                acertions.append('_')
        return acertions

    letter = input('>')
    result = lienarSearch(palabra,listLen,letter)
    
    if(result):
        for i in result:
            if(i != '_'):
                progreso = progreso + palabra[i]
            else:
                progreso = progreso + ' _ '
    else:
        print("Not found")
    print(progreso)