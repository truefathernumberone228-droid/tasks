import sys

# Чтение данных эллипса
with open(sys.argv[1], "r") as f:
    x0, y0 = map(float, f.readline().split())
    a, b = map(float, f.readline().split())

# Чтение точек
with open(sys.argv[2], "r") as f:
    points = [tuple(map(float, line.split())) for line in f if line.strip()]

eps = 1e-9

for x, y in points:
    value = ((x - x0) ** 2) / (a ** 2) + ((y - y0) ** 2) / (b ** 2)

    if abs(value - 1) < eps:
        print(0)
    elif value < 1:
        print(1)
    else:
        print(2)