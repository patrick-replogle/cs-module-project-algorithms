'''
Input: an integer
Returns: an integer
'''


cache = {}


def eating_cookies(n, memoize=None):
    if n in cache:
        return cache[n]
    else:
        if n == 0:
            return 1
        if n < 0:
            return 0

        result = eating_cookies(
            n-1) + eating_cookies(n-2) + eating_cookies(n-3)
        cache[n] = result

        return cache[n]


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
