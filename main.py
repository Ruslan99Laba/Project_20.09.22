# 1
height1 = int(input("Введите ввысоту треугольника слева: "))//2+1
weight1 = height1

for h in range(height1):
    for w in range(h + 1):
        print('*', end="  ")
    print()
for h in range(height1, 0, -1):
    for w in range(h - 1):
        print('*', end="  ")
    print()

# 2
height2 = int(input("Введите ввысоту треугольника снизу: "))//2+1
weight2 = height2 * 2 - 1

for h in range(height2):
    for w in range(weight2):
        if h + w <= height2 - 2:
            print('  ', end=" ")
            continue
        if w - h <= height2 - 1:
            print('*', end="  ")
            continue
        print(' ', end=" ")
    print()

# 3
height3 = int(input("Введите ввысоту треугольника справа: "))//2+1
weight3 = height3

for h in range(height3):
    for w in range(weight3):
        if h + w >= weight3:
            print('*', end="  ")
            continue
        print(' ', end="  ")
    print()
for h in range(height3, 0, -1):
    for w in range(weight3):
        if h + w >= weight3:
            print('*', end="  ")
            continue
        print(' ', end="  ")
    print()

# 4
height4 = int(input("Введите ввысоту треугольника сверху: "))//2+1
weight4 = height4 * 2 - 1

for h in range(height4):
    for w in range(weight4):
        if w < h:
            print(' ', end="  ")
            continue
        if w + h >= weight4:
            print(' ', end="  ")
            continue
        print('*', end="  ")
    print()
