from functools import reduce

DIGITS = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}


def intCount(s):
    return reduce(lambda x, y: x * 10 + y, map(lambda x: DIGITS[x], s))


def str2float(s):
    dot_index = s.find(".")
    ints = s[:dot_index]
    fractions = s[dot_index + 1 :]
    return intCount(ints) + intCount(fractions) / (10 ** len(fractions))


print("str2float('123.456') =", str2float("123.456"))
if abs(str2float("123.456") - 123.456) < 0.00001:
    print("测试成功!")
else:
    print("测试失败!")
