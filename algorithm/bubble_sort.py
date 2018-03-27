# -*- coding: utf-8 -*-


def sort(no_sort_list):
    for j in range(len(no_sort_list) - 1):
        for i in range(len(no_sort_list) - 1 - j):
            if no_sort_list[i] > no_sort_list[i + 1]:
                tmp = no_sort_list[i + 1]
                no_sort_list[i + 1] = no_sort_list[i]
                no_sort_list[i] = tmp


if __name__ == '__main__':
    num_list = [1, 0, 8, 11, -8, 2, 1, 10, 12]
    sort(num_list)
    print(num_list)
