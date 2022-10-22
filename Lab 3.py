#Tom Steinman
#003L
#Lab 3

print('Welcome to the Flarsheim Guesser!')

while True:

    print('\nPlease think of a number between and including 1 and 100.\n')

    while True:
        rem3 = int(input('What is the remainder when your number is divided by 3?'))
        if rem3 < 0:
            print('The value entered must be 0 or greater')
            continue
        elif rem3 >= 3:
            print('The value entered must be less than 3')
            continue
        else:
            print()
            break

    while True:
        rem5 = int(input('What is the remainder when your number is divided by 5?'))
        if rem5 < 0:
            print('The value entered must be 0 or greater')
            continue
        elif rem5 >= 5:
            print('The value entered must be less than 5')
            continue
        else:
            print()
            break

    while True:
        rem7 = int(input('What is the remainder when your number is divided by 7?'))
        if rem7 < 0:
            print('The value entered must be 0 or greater')
            continue
        elif rem7 >= 7:
            print('The value entered must be less than 7')
            continue
        else:
            print()
            break

    for num in range(0, 101):
        if num % 3 == rem3:
            if num % 5 == rem5:
                if num % 7 == rem7:
                    print(f'Your number is {num}')
                    print('How amazing is that?\n')

    while True:
        replay = (input('Do you want to play again? Y to continue, N to quit ==> '))
        if replay == 'Y' or replay == 'y':
            break
        elif replay == 'N' or replay == 'n':
            exit()
        else:
            continue

    continue