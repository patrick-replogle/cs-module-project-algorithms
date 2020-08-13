'''
Input: an integer
Returns: an integer
'''


def eating_cookies(n, arr=[]):
    if n == 0:
        return 1

    if n < 0:
        return 0

    if arr[n]:
        return arr[n]

    else:
        arr[n] = eating_cookies(
            n-1, arr) + eating_cookies(n-2, arr) + eating_cookies(n-3, arr)

        return arr[n]


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies, [0 for _ in range(num_cookies + 1)])} ways for Cookie Monster to eat {num_cookies} cookies")
