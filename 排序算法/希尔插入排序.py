# 渣渣葡萄
# 开发时间：2021/10/15 16:47
"""
插入排序核心思想 将数组分成一个有序数组和一个无序数组 每次从无序数组中提一个元素出来 插入到 有序元素的合适位置
"""
from typing import List


def insert_sort(arr: List) -> List:
    """
     插入排序
    :param arr:
    :return:
    """
    target = []
    l = len(arr)
    for i in range(l):
        insert_index = 0
        for j in range(len(target)):
            if arr[j] >= arr[i]:
                break
            insert_index += 1
        target.insert(insert_index, arr[i])
    return target


def insert_sort_by_org_arr(arr: List) -> List:
    """
    插入排序 原数组上改
    :param arr:
    :return:
    """
    l = len(arr)
    for i in range(l):
        insert_index = i - 1
        insert_val = arr[i]
        while insert_index >= 0 and arr[insert_index] > insert_val:
            arr[insert_index + 1] = arr[insert_index]
            insert_index -= 1
        arr[insert_index + 1] = insert_val


if __name__ == '__main__':
    arr = [4, 1, 5, 7, 6, -1, 55, -55, 666]
    print(insert_sort(arr))
    insert_sort_by_org_arr(arr)
    print(arr)
