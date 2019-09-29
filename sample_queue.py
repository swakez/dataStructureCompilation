
import queue

marco_queue = queue.Queue(100)

try:
    n = int(input())
except:
    print('Invalid input')
    exit()

for i in range(n):
    op = input().split()
    if op[0].upper() == 'D':
        if(not marco_queue.empty()):
            print(f"{marco_queue.get()} {(marco_queue.qsize())}")
            print("EMPTY")
    elif op[0].upper() == 'E':
        if not marco_queue.full():
            marco_queue.put(int(op[1]))
            print(marco_queue.qsize())
        else:
            print("FULL")
