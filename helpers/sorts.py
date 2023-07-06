from typing import List


# SELECTION SORT

# the current element will be compared to what's after it, and the minimum element will be placed
# at the current position
# no matter what, current element will be compared with every element that's after it
# resulting in a complexity of .. O(n*(n+1)/2) = O(n^2)

def selection_sort_brute_force(nums: List[int]) -> List[int]:
    length = len(nums)

    # it's like calculating the minimum for the i-th position
    # on each iteration (compares with j-th element and swaps each time)
    # performs redundant swaps.. but.. works
    for i in range(length):
        for j in range(i + 1, length):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]

    return nums


def selection_sort_smarter(nums: List[int]) -> List[int]:
    length = len(nums)

    # it's like calculating the minimum for the i-th position
    # on each iteration (compares with j-th element and swaps each time)
    for i in range(length):
        min_idx = i
        for j in range(i + 1, length):
            if nums[min_idx] > nums[j]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]

    return nums


# INSERTION SORT

# each iteration, the current element will be put
# wherever it fits in the part of the array that was already sorted


def insertion_sort(nums: List[int]) -> List[int]:
    # consider that the sorted (starting) array is of length 1 (first number in the list)
    length = len(nums)

    for i in range(1, length):
        # saving current value, it'll get overwritten if the value isn't greater than what's before
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key

    return nums


# BUBBLE SORT
# works just like bubbles in beers go from bottom to top (except guinness)

def bubble_sort(nums: List[int]) -> List[int]:
    # if we didn't swap something me might just break - it means that the array has been sorted
    length = len(nums)
    for i in range(length - 1):
        swapped_something = False

        for j in range(length - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped_something = True

        if not swapped_something:
            break

    return nums


# MERGE SORT
# recursively split array in two, sort, then merge

def merge(first_half: List[int], last_half: List[int]) -> List[int]:
    i, j = 0, 0
    m, n = len(first_half), len(last_half)
    res = []
    while i < m and j < n:
        if first_half[i] < last_half[j]:
            res.append(first_half[i])
            i += 1
        else:
            res.append(last_half[j])
            j += 1

    while i < m:
        res.append(first_half[i])
        i += 1

    while j < n:
        res.append(last_half[j])
        j += 1

    return res


def merge_sort(nums: List[int]) -> List[int]:
    length = len(nums)

    if length == 1 or length == 0:
        return nums

    m = length // 2

    left = merge_sort(nums[:m])
    right = merge_sort(nums[m:])

    return merge(left, right)


# QUICK SORT
# works by selecting a pivot
# and assuring that all elements to the left are lesser than the pivot
# and that all elements to the right are greater than the pivot

# Function to find the partition position
def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)


def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high

    while True:
        while i <= j and arr[i] <= pivot:
            i += 1

        while i <= j and arr[j] >= pivot:
            j -= 1

        if i > j:
            break
        arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]
    return j


if __name__ == "__main__":
    test_arr = [7, 6, 5, 5, 5, 55, 5, 5, -23, 3, 2, 1]
    # print(selection_sort_brute_force(test_arr))
    # print(selection_sort_smarter(test_arr))
    # print(insertion_sort(test_arr))
    # print(bubble_sort(test_arr))
    # print(merge_sort(test_arr))
    print(test_arr)
    quick_sort(test_arr, 0, len(test_arr) - 1)
    print(test_arr)
