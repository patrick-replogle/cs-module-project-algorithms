#!/usr/bin/python

import sys

cache = {}
cache[0] = 1


# solution works with amounts up to 1000
def making_change(amount, denominations):
    if (amount, len(denominations)) in cache:
        return cache[(amount, len(denominations))]

    if amount == 0:
        return 1

    if amount < 0:
        return 0

    else:
        count = 0
        for i in range(len(denominations)):
            count += making_change(amount -
                                   denominations[i], denominations[i:])

        cache[(amount, len(denominations))] = count
        return count


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
