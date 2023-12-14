import os
import threading
import multiprocessing
import time

from utilis import generate_large_text_file

def execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        print(f'The function executed in {end_time - start_time} seconds')
        return res
    return wrapper


def count_words_in_chunk(chunk, word_freq):
    for word in chunk.split():
        word_freq[word] = word_freq.get(word, 0) + 1
    return word_freq


def process_file_chunk(start, end, filename):
    with open(filename, 'r') as file:
        file.seek(start)
        text = file.read(end - start)
        word_freq = {}
        count_words_in_chunk(text, word_freq)
        return word_freq


@execution_time
def count_words_simple(filename):
    word_freq = {}
    with open(filename, 'r') as file:
        for line in file:
            count_words_in_chunk(line, word_freq)
    return word_freq


@execution_time
def count_words_multithreading(filename, num_threads=10):
    word_freq = {}
    threads = []
    with open(filename, 'r') as file:
        file_content = file.read()
        chunk_size = len(file_content) // num_threads
        for i in range(0, len(file_content), chunk_size):
            chunk = file_content[i:i+chunk_size]
            thread = threading.Thread(target=count_words_in_chunk, args=(chunk, word_freq))
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()

    return word_freq


@execution_time
def count_words_multiprocessing(filename, num_processes=10):
    file_size = os.path.getsize(filename)
    chunk_size = file_size // num_processes
    tasks = []

    with multiprocessing.Pool(num_processes) as pool:
        for i in range(0, file_size, chunk_size):
            start = i
            end = min(i + chunk_size, file_size)
            task = pool.apply_async(process_file_chunk, (start, end, filename))
            tasks.append(task)

        results = [task.get() for task in tasks]

    word_freq = {}
    for result in results:
        for word, count in result.items():
            word_freq[word] = word_freq.get(word, 0) + count

    return word_freq


if __name__ == '__main__':
    file_name = 'large_text.txt'
    if not os.path.exists(file_name):
        print(f"File {file_name} not found. Generating new file...")
        generate_large_text_file(file_name)
    else:
        print(f"File {file_name} already exists. Proceeding with existing file.")

    print('\nSimple count')
    count_words_simple(file_name)
    print('\nMultithreading count')
    count_words_multithreading(file_name)
    print('\nMultiprocessing count')
    count_words_multiprocessing(file_name)

