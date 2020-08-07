'''
Input: a List of integers
Returns: a List of integers
'''


# third pass solution
def moving_zeroes(arr):
    arr.sort(reverse=True)
    for i in range(len(arr)):
        if arr[i] == 0:
            arr[i], arr[len(arr) - 1] = arr[len(arr) - 1], arr[i]
    return arr


# first pass solution
# def moving_zeroes(arr):
#     positive = []
#     negative = []
#     zero = []

#     for i in range(len(arr)):
#         if arr[i] > 0:
#             positive.append(arr[i])
#         elif arr[i] < 0:
#             negative.append(arr[i])
#         else:
#             zero.append(arr[i])

#     return positive + negative + zero


# second pass
# def moving_zeroes(arr):
#     for i, val in enumerate(arr):
#         if val > 0:
#             arr.pop(i)
#             arr.insert(0, val)
#         elif val == 0:
#             arr.pop(i)
#             arr.append(val)
#     return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]  # => [3, 1, -2, 0, 0]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
