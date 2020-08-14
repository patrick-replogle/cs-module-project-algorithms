'''
Input: a List of integers
Returns: a List of integers
'''


# first pass solution
def product_of_all_other_numbers(arr):
    string = '*'.join(map(str, arr))
    n = len(arr) - 1

    for i in range(len(arr)):
        if i != n:
            arr[i] = eval(string.replace(str(arr[i]) + "*", "", 1))
        elif i == n:
            arr[i] = eval(string.replace('*' + str(arr[i]), "", 1))
    return arr


# similar and less efficient solution
# def product_of_all_other_numbers(arr):
#     output = ""
#     for i in range(len(arr)):
#         if i != len(arr) - 1:
#             output += f'{arr[i]}*'
#         else:
#             output += f'{arr[i]}'

#     for i in range(len(arr)):
#         if i != len(arr) - 1:
#             arr[i] = eval(output.replace(str(arr[i]) + '*', "", 1))
#         else:
#             arr[i] = eval(output.replace('*' + str(arr[i]), "", 1))
#     return arr


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    # arr = [1, 7, 3, 4]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]
    arr = [7, 9, 1, 8, 6, 7, 8, 8, 7, 10]
    expected = [13547520, 10536960, 94832640, 11854080, 15805440,
                13547520, 11854080, 11854080, 13547520, 9483264]

    print(
        f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
