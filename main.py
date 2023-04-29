from os import system
from threading import Thread
from time import sleep

from helpers import get_words
from db import DB

run = False
count = 0
wrong = 0

# Init DB
db = DB('store.db')
db.init()


# Print help command
def print_commands():
    print("Enter: \n- s to start \n- st - to print your stat \n- Ctrl+C to exit \n")


# Print stat
def print_stat():
    data = db.get_data()
    print(f"\nYour record - {data[3]} \nAttempts - {data[1]} \nWrong words - {data[2]} \n")


# Start type test
def start_test():
    global run
    global count
    global wrong
    
    system('cls')
    words = get_words(300)
    run = True

    test = Thread(target=start_typing, args=(words,))
    test.start()

    sleep(60)

    run = False
    test.join()

    db.update_data(wrong_words=wrong, increase_update=True)

    record = db.get_data()[-1]
    if count > record:
        print("Congratulate! You have beat your record!")
        db.update_data(record=count)
    print(f"Your score is {count}\n")

    count = 0
    wrong = 0


# Listening inputs and count words
def start_typing(words):
    global count
    global wrong

    k = 0

    while run:
        word = words[k]
        print(word)
        input_word = input(': ')

        if word.replace('\n', '') == input_word.strip(): count += 1
        else: wrong += 1

        k += 1
        system('cls')


# Start program
def main():
    print("Hello! This is type speed test.")
    print("You should type words as possible as faster.\n")
    print_commands()

    while True:
        action = input("Input an action: ")

        if action == 's':
            start_test()
            print_commands()
        
        if action == 'st':
            print_stat()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram was stopped")
