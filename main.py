import os
import platform
import time

def clear():
    if platform.system() == 'Linux':
        os.system('clear')
    elif platform.system() == 'Darwin':
        os.system('clear')
    elif platform.system() == 'Windows':
        os.system('cls')

def start():
    print('Welcome to the calculator. Choose an option: ')
    print("Type 'r' to run the program.")
    print("Type 'q' to quit the program.")

    run = input('> ')

    if run == 'r':
        print('Starting calculator...')
        time.sleep(2)
        print('Assembling libraries...')
        time.sleep(1)
        print('Almost done...')
        time.sleep(1)
        clear()
        calc()
    elif run == 'q':
        clear()
        print('Thanks for using the calculator. See you soon! (Ending in 3...)')
        time.sleep(3)
        exit()
    else:
        print('WARNING: Unexpected input. Closing program in 3...')
        time.sleep(3)
        exit()

def calc():
    print('Welcome to the Calculator. Good luck!')

    print('Enter first number: ')
    num1 = int(input('> '))

    print('Enter second number: ')
    num2 = int(input('> '))

    print('Storing values...')
    time.sleep(2)
    clear()

    print('Your numbers are: ',str(num1),'and ', str(num2))
    time.sleep(2)
    print('Choose an operator: ')
    print("'a' for Addition.")
    print("'s' for Subtraction.")
    print("'m' for Multiplication.")
    print("'d' for Division.")
    print("'e' for Exponentiation.")
    print("'mo' for Modulus.")
    print("'fd' for Floor Division.")

    oper = input('> ')

    if oper == 'a':
        sum = num1+num2
        print('The sum is: ', sum)
        res()
    elif oper == 's':
        diff = num1-num2
        print('The difference is: ', diff)
        res()
    elif oper == 'm':
        prod = num1*num2
        print('The product is: ', prod)
        res()
    elif oper == 'd':
        quot = num1/num2
        print('The quotient is: ', quot)
        res()
    elif oper == 'e':
        exp = num1**num2
        print('The answer is: ', exp)
        res()
    elif oper == 'mo':
        mod = num1%num2
        print('The answer is: ', mod)
        res()
    elif oper == 'fd':
        fdq = num1//num2
        print('The answer is: ', fdq)
        res()
    else:
        print('WARNING: Unexpected input. Closing program in 3...')
        time.sleep(3)
        exit()


def res():
    print('Do you want to start the program again? (y/n)')
    choice = input('> ')

    if choice == 'y':
        print('Restarting program in 3...')
        time.sleep(3)
        clear()
        start()
    if choice == 'n':
        clear()
        print('Thank you for using the program! (Ending in 3...)')
        time.sleep(3)
        exit()


start()
