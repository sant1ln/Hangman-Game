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
random_word = 'ana'
palabra = []
print('Juego del ahorcado')
for letra in random_word:
    palabra.append(letra)

listLen = len(palabra)
acertions = []
for a in range(0,listLen):
    acertions.append(' _ ')

while(game == False):
    

    def lienarSearch(palabra,listLen,letter):
        
        for i in range(0,listLen):
            if(palabra[i] == letter and letter not in acertions[i]):
                    acertions[i] = palabra[i]
        return acertions

    
    finalString = ''.join(acertions)
    print('D',finalString)
    if(finalString == random_word):
        print('Good Job!')
        game = True
        break
    
    letter = input('>')
    lienarSearch(palabra,listLen,letter)

            
    
    