from multiprocessing import Process, Queue
from random import randint
from time import time


def task_handle(cur_list, result_queue):
    total = 0
    for number in cur_list:
        total += number
    result_queue.put(total)


def main():
    processes = []
    number_list = [x for x in range(1, 10000001)]
    result_queue = Queue()
    index = 0

    for _ in range(8):
        p = Process(target=task_handle,
                    args=(number_list[index:index + 125000], result_queue))
        index += 125000
        processes.append(p)
        p.start()

    start = time()
    for p in processes:
        p.join()
    total = 0
    while not result_queue.empty():
        total += result_queue.get()
    print('----total-------')
    print(total)

    end = time()

    print('Excusion: %.3f' % (end - start))


if __name__ == '__main__':
    main()
