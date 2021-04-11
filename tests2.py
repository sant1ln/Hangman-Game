game = False
progreso = []
palabra = 'python'
""" palabra = []
for letra in random_word:
    palabra.append(letra) """

listLen = len(palabra)
acertions = '_'*listLen
""" for a in range(0,listLen):
    acertions.append('_')
letters_done = [] """

while(game == False):
    

    def lienarSearch(palabra,listLen,letter):
        
        for i in range(0,listLen):
            if(palabra[i] == letter and letter not in acertions):
                    acertions[i] = palabra[i]
            # else:
            #     acertions.append('_')
        return acertions

    
    print('D',acertions)
    letter = input('>')
    lienarSearch(palabra,listLen,letter)