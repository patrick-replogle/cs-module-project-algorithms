'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


# first solution
def single_number(arr):
    for val in arr:
        if arr.count(val) == 1:
            return val


# second solution
# def single_number(arr):
#     unique = set()
#     for val in arr:
#         if val in unique:
#             unique.remove(val)
#         else:
#             unique.add(val)
#     return unique.pop()


print(single_number([1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]))
if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
