'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

# first pass solution works, but doesn't perform well with large data sets
# def sliding_window_max(nums, k):
#     result = []

#     for i in range(len(nums) - k + 1):
#         result.append(max(nums[i: i + k]))

#     return result


# another slow solution with large data sets
# def sliding_window_max(nums, k):
#     result = []

#     for i in range(len(nums) - k + 1):
#         max_num = nums[i]
#         j = i
#         while j < i + k:
#             if nums[j] > max_num:
#                 max_num = nums[j]
#             j += 1
#         result.append(max_num)

#     return result


def sliding_window_max(nums, k):
    queue = []
    results = []
    m = 0

    for i in range(len(nums)):
        while len(queue) > m and nums[queue[-1]] <= nums[i]:
            queue.pop()

        queue.append(i)

        if i >= k-1:
            results.append(nums[queue[m]])
            if i - queue[m] >= k - 1:
                m += 1

    return results


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    expected_output = [3, 3, 5, 5, 6, 7]

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
