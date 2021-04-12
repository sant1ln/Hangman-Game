import random
import os

def read_data():
    words = []
    with open("./data.txt","r",encoding="utf-8") as data:
        for word in data:
            actual_word = word.replace("\n",'')
            words.append(actual_word)
    return words

def select_random_word(words):
    random_number = random.randrange(0, 171)
    random_word = words[random_number]
    without_acents = random_word.maketrans('áéíóú', 'aeiou')
    remove_acents = random_word.translate(without_acents)
    random_word = remove_acents
    return random_word

def game_core(random_word):
    game = False
    palabra = []
    
    for letra in random_word:
        palabra.append(letra)

    listLen = len(palabra)
    acertions = []
    for a in range(0,listLen):
        acertions.append(' _ ')
        

    while(game == False):
        os.system('cls')
        os.system('clear')

        def lienarSearch(palabra,listLen,letter):
            
            for i in range(0,listLen):
                if(palabra[i] == letter and letter not in acertions[i]):
                        acertions[i] = palabra[i]
            return acertions

        
        finalString = ''.join(acertions)
        if(finalString == random_word):
            print('Good Job!')
            print('Word: ',random_word)
            game = True
            break
        print('Hangman game (ಠ_ಠ)')
       
        print('>',finalString.capitalize())
        letter = input('Ingresa una letra: ').lower()
        lienarSearch(palabra,listLen,letter)

def run():
    words = read_data()
    random_word = select_random_word(words)
    game_core(random_word)

if __name__ == '__main__':
    run()