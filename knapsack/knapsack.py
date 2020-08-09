#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])


def knapsack_solver(items, capacity):
    items.sort(key=lambda x: x[2] / x[1], reverse=True)
    knapsack = []
    value = 0
    weight = 0

    for item in items:
        if weight + item.size <= capacity:
            knapsack.append(item.index)
            weight += item.size
            value += item.value

    knapsack.sort()
    return {'Value': value, 'Chosen': knapsack}


if __name__ == '__main__':
    if len(sys.argv) > 1:
        capacity = int(sys.argv[2])
        file_location = sys.argv[1].strip()
        file_contents = open(file_location, 'r')
        items = []

        for line in file_contents.readlines():
            data = line.rstrip().split()
            items.append(Item(int(data[0]), int(data[1]), int(data[2])))

        file_contents.close()
        print(knapsack_solver(items, capacity))
    else:
        print('Usage: knapsack.py [filename] [capacity]')
