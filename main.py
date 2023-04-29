from os import system
from threading import Thread
from time import sleep
from random import choice

run = False
count = 0

def get_words(k):
    words = []
    with open('words.txt', 'r') as f:
        all_words = f.readlines()

        for _ in range(100):
            word = choice(all_words)
            words.append(word)
    return words


def start_test():
    global run
    system('cls')
    words = get_words(300)
    run = True

    test = Thread(target=start_typing, args=(words,))
    test.start()

    sleep(60)

    run = False
    test.join()


def start_typing(words):
    global count
    k = 0

    while run:
        word = words[k]
        print(word)
        input_word = input(': ')
        if word.replace('\n', '') == input_word.strip():
            count += 1
        k += 1
        system('cls')
    
    print(f"Your score is {count}\n")
    count = 0

def log_commands():
    print("Enter: \n- s to start \n- Ctrl+C to exit\n")

def main():
    print("Hello! This is type speed test.")
    print("You should type words as possible as faster.\n")
    log_commands()

    while True:
        action = input("Input an action: ")

        if action == 's':
            start_test()
            log_commands()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram was stopped")
