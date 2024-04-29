RED = "\33[91m"
GREEN = "\033[32m"
RESET = "\033[0m"
YELLOW = "\033[33m"

from collections import deque

def is_palindrome(item):

    str = ''.join(i.lower() for i in item if i.isalpha())

    deq = deque(str)

    while len(deq) > 1:
        if deq.pop() != deq.popleft():
            return False 
    return True


def test_is_palindrome(list):
    qounter = 0
    for item in list:
        if is_palindrome(item):
            print(f'{GREEN}{item} - Паліндром{RESET}')
            qounter +=1
        else:
            print(f'{RED}{item} - Не є паліндромом{RESET}')
    print(f'''{YELLOW}
Кількість елементів у списку: {len(list)}
Всього паліндромів у списку: {qounter}{RESET}''')

list = [
    "Anna",
    "civic",
    "taco cat",
    "my gym",
    "red rum, sir, is murder",
    "no lemon, no melon",
    "never odd or even",
    "Sit on a potato pan, Otis.",
    "Madam, I'm Adam.",
    "Able was I, ere I saw Elba.",
    "chicken, monkey!",
    "Check String is Palindrome"
]

test_is_palindrome(list)