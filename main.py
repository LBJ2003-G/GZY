def bubble_sort(arr):
    n = len(arr)
    # 外层循环控制需要遍历的次数
    for i in range(n):
        # 内层循环控制每次遍历需要比较的次数
        # 每次遍历后，最大的元素会被放到最后，所以下一轮可以少比较一次
        for j in range(0, n - i - 1):
            # 如果前面的元素大于后面的元素，则交换它们的位置
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# 测试代码
if __name__ == "__main__":
    # 创建一个测试数组
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print("原始数组:", test_array)
    
    # 调用冒泡排序函数
    sorted_array = bubble_sort(test_array)
    print("排序后数组:", sorted_array) 