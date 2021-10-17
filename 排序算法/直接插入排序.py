# 渣渣葡萄
# 开发时间：2021/10/15 16:32
def InsertSort(input_list):
    if len(input_list) == 0:
        return []
    sorted_list = input_list
    for i in range(1, len(input_list)):
        # 将待排元素赋给临时变量
        temp = sorted_list[i]
        # 从待排元素前一个元素开始寻找temp的合适位置
        j = i - 1
        # 没有找到合适位置就让将空出的位置向前移动
        while j >= 0 and temp < sorted_list[j]:
            sorted_list[j + 1] = sorted_list[j]
            j -= 1
        # 找到合适位置将temp放在该位置
        # 因为循环里是先移动再让j减一了，故合适位置应该在j+1的位置
        sorted_list[j + 1] = temp

        print("%dth" % i)
        print(sorted_list)
    return sorted_list


if __name__ == '__main__':
    input_list = [50, 123, 543, 187, 49, 30, 0, 2, 11, 100]
    print("input_list:")
    print(input_list)
    sorted_list = InsertSort(input_list)
    print("sorted_list:")
    print(sorted_list)