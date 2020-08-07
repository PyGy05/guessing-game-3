from random import randint
import sys
sys.argv


# generate a number 1~10
answer = randint(int(sys.argv[1]), int(sys.argv[2]))
g1 = int(sys.argv[1])
g2 = int(sys.argv[2])
# input from user?
# print(g1)
# print(g2)

# check that an input is number g1~g2
while True:
    try:
        print(answer)
        guess = int(input(f'guess a number {g1} ~ {g2}: '))
        if g1 < guess < g2:
            if guess == answer:
                print('you are a genius!  ')
                break
        else:
            print('hey bozo you said', g1, '~', g2)
    except ValueError:
        print('please enter a number')
        continue
    break

# check if number is rite guess. Otherwise
# ask again
