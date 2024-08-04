weight = input('weight is(kg):')
hight = input('hight is(m):')
weightNum = float(weight)
hightNum = float(hight)
bmi = weightNum/(hightNum**2)
print('bmi is ',bmi)
if bmi <18.5:
    print('bmi is ',bmi)
    print('you are too thin.')
elif bmi < 25:
    print('bmi is ',bmi)
    print('you weight is very fine')
elif bmi < 28:
    print('bmi is ',bmi)
    print('you are a little fat.')
elif bmi <32:
    print('bmi is ',bmi)
    print('you are too fat.')
else:
    print('bmi is ',bmi)
    print('you must start to lose weight right now!')