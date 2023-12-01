import time
import random


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time of {func.__name__}: {execution_time} seconds")
        return result
    return wrapper

@measure_time
def filter_numbers(line):
    numbers = list(map(int, line.split()))
    filtered_numbers = list(filter(lambda x: x > 40, numbers))
    return ' '.join(map(str, filtered_numbers))

@measure_time
def read_file_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

if __name__=="__main__":
    with open('random_numbers.txt', 'w') as file:
        for _ in range(100):
            line = ' '.join(str(random.randint(1, 100)) for _ in range(20))
            file.write(line + '\n')

    with open('random_numbers.txt', 'r') as file:
        lines = file.readlines()

    filtered_lines = list(map(filter_numbers, lines))

    with open('filtered_numbers.txt', 'w') as file:
        file.writelines('\n'.join(filtered_lines))

    for line in read_file_generator('filtered_numbers.txt'):
        print(line)
