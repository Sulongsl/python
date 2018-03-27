# -*- coding: utf-8 -*-

"""
分治递归
"""


def quick_sort(arr, low, high):
    if low < high:
        # 获取基准值坐标
        key_index = partition(arr, low, high)
        # 对基准值数组进行拆分
        quick_sort(arr, low, key_index - 1)
        # 对基准值右边进行分组
        quick_sort(arr, key_index + 1, high)


"""
将数据按基准值分组
之后返回基准值坐标
"""


def partition(arr, low, high):
    # 基准值
    key = arr[low]
    # 外层循环
    while low < high:
        # 从右到左,查找小于基准值的
        while low < high and arr[high] >= key:
            high -= 1
        if low < high:
            arr[low] = arr[high]

        # 从左到右,查找小于基准值的
        while low < high and arr[low] < key:
            low += 1
        if low < high:
            arr[high] = arr[low]
    # 基准值在数组中所在位置
    arr[low] = key
    # 返回基准值坐标
    return low


"""
main方法
"""
if __name__ == '__main__':
    arr = [8, 7, 1, 4, 2, 3, 6, 5, 9, 0, 6]
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)
