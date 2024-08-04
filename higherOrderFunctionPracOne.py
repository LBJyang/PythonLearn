def normalize(name):
    _name = name.lower()
    return _name[:1].upper() + _name[1:]


# 测试:
L1 = ["adam", "LISA", "barT"]
L2 = list(map(normalize, L1))
print(L2)
