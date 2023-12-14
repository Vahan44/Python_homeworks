import random
import string


def generate_large_text_file(filename, size=1000000):
    with open(filename, 'w') as file:
        for _ in range(size):
            word = ''.join(random.choices(string.ascii_lowercase + ' ', k=random.randint(1, 10)))
            file.write(word + '\n')