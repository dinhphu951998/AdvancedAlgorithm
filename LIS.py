import math

global_lis = 0
def lis_recursive(arr: list[int], i: int, currentMax: int, currentLis: int):
    """
    Longest Increasing Subsequence
    Find the longest subsequence of a given sequence in which the subsequence's elements are in sorted order, lowest to highest

    Time: O(2^n)
    Space: O(1)
    """
    global global_lis
    if i == len(arr):
        return
    if arr[i] > currentMax:
        global_lis = max(global_lis, currentLis + 1)
        lis_recursive(arr, i + 1, arr[i], currentLis + 1)
    lis_recursive(arr, i + 1, currentMax, currentLis)


# Time: O(n^2)
# Space: O(n)
def lis_dp(nums):
    n = len(nums)
    # Store the length of LIS
    lis = [0] * n

    for i in range(n):
        j = i - 1

        # Find elements at least as large as nums[i]
        while j >= 0:
            if nums[j] < nums[i]:
                lis[i] = max(lis[i], lis[j] + 1)
            j -= 1

        # Init lis = 1 if nums[i] not greater than any of the previous elements
        if j < 0 and lis[i] == 0:
            lis[i] = 1
    return max(lis)

arr = [1, 2, 3, 4, 9, 10, 5, 6, 7]
print(lis_dp(arr)) # output: 7

