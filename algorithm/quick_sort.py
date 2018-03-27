# -*- coding: utf-8 -*-

def quick_sort(arr, low, high):
    if low < high:
        key_index = partition(arr, low, high)
        quick_sort(arr, low, key_index - 1)
        quick_sort(arr, key_index + 1, high)


def partition(arr, low, high):
    key = arr[low]
    while low < high:
        while low < high and arr[high] >= key:
            high -= 1
        if low < high:
            arr[low] = arr[high]

        while low < high and arr[low] < key:
            low += 1
        if low < high:
            arr[high] = arr[low]
    arr[low] = key
    return low


if __name__ == '__main__':
    arr = [8, 7, 1, 4, 2, 3, 6, 5, 9, 0, 6]
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)
