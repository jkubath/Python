# Summary: This is a python program that uses multiple processes
# Author: Jonah Kubath
# Date: 05/27/2018

import multiprocessing

def spawn(num, num2):
    print('Spawn # {} {}'.format(num, num2))

if __name__ == '__main__':
    for i in range(5):
        p = multiprocessing.Process(target=spawn, args=(i, i+1))
        p.start()