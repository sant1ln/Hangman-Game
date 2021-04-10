import random

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
    return random_word


def game_core(random_word):
    user_input = input('Ingrese una letra')
    print(random_word.includes(user_input))

def run():
    words = read_data()
    random_word = select_random_word(words)
    game_core(random_word)

if __name__ == '__main__':
    run()