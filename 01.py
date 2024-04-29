RED = "\33[91m"
GREEN = "\033[32m"
RESET = "\033[0m"
YELLOW = "\033[33m"

from queue import Queue
import time
import random

class Order:
    def __init__(self, id):
        self.id = id
    
    def __str__(self):
        return str(self.id)


def generate_request(id,stack):
    order = Order(id)
    stack.put(order)
    print(f'{GREEN}Додали в чергу заявку: {order.id}{RESET}')

def process_request(stack):
    if not stack.empty():
        order = stack.get()
        print(f'{GREEN}Обробили та видалили з черги заявку: {order}{RESET}')
        time.sleep(random.uniform(0.3,1.5))
    else:
        print(f'''
{RED}Черга пуста{RESET}
              ''')

def generate():
    id = 0
    stack = Queue()
    try:
        while True:
            time.sleep(0.75)

            if random.choice([True, False]):
                id +=1
                generate_request(id,stack)

            if random.choice([True, False]):
                process_request(stack)
    except KeyboardInterrupt: 
        print(f'''{YELLOW}
Симуляція закінчена{RESET}''')
        
generate()   