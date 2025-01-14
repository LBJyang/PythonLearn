def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    for i, value in enumerate(L):
        if i == 0:
            minnum = value
            maxnum = value
        if value > maxnum:
            maxnum = value
        if value < minnum:
            minnum = value
    return (minnum, maxnum)


# 测试
if findMinAndMax([]) != (None, None):
    print("测试失败!")
elif findMinAndMax([7]) != (7, 7):
    print("测试失败!")
elif findMinAndMax([7, 1]) != (1, 7):
    print("测试失败!")
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print("测试失败!")
else:
    print("测试成功!")
