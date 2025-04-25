def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = a + b, a
        yield a


fibb = fib(10)
for i in fibb:
    print(i, end=' ')
print('\n')


def binary_search(li, target):
    low, high = 0, len(li) - 1
    while low <= high:
        mid = (low + high) // 2
        if li[mid] == target:
            return mid
        elif li[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


li1 = [1, 2, 3, 4, 5, 9, 14, 17, 29, 35]
print(binary_search(li1, 14))

# 快速
li2 = [3, 5, 7, 26, 35, 16, 35, 46, 37, 89, 69]


def quick_sort(li):
    if len(li) <= 1:
        return li
    mid = li[len(li) // 2]
    left = [x for x in li if x < mid]
    right = [x for x in li if x > mid]
    middle = [x for x in li if x == mid]
    return quick_sort(left) + middle + quick_sort(right)


print(quick_sort(li2))

# 冒泡
li3 = [13, 7, 5, 26, 35, 16, 35, 46, 37, 89, 69]
print(li3)
for n in range(len(li3) - 1):
    for m in range(n + 1, len(li3)):
        if li3[m] < li3[n]:
            li3[n],li3[m] = li3[m], li3[n]
    print(li3)
# print("冒泡排序：", li3)


# 1234 四个数字可以组成哪些3位数 不重复
# 分析：个位十位百位 每一位都可能是1234
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != j and i != k and j != k:
                print(i, j, k)
