import socket
import random
import os

def unique_random_n_digits(digit: int, cur_digit: set()):
    start = 10**(digit - 1)
    end = (10**digit) - 1
    num = random.randint(start, end)
    if len(cur_digit) == end - start + 1:
        return False
    else:
        while num in cur_digit:
            num = random.randint(start, end)
        return num

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]
    
def iterateFilesFromDir(path: str, file_type: str = None):
    for root, _, files in os.walk(path):
        for file in files:
            if file_type is not None:
                if file_type in file:
                    yield os.path.join(root, file)
            else:
                yield os.path.join(root, file)

if __name__ == "__main__":
    import timeit
    print(timeit.timeit("unique_random_n_digits(1, {1, 2, 3, 4, 5, 6, 7, 8})", setup="from __main__ import unique_random_n_digits", number=10000))
    print(unique_random_n_digits(1, {1, 2, 3, 4, 5, 6, 7, 8, 9}))