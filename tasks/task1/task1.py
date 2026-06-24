import sys


def get_path(n, m):
    path = []
    current = 1

    while True:
        path.append(str(current))

        current = ((current + m - 2) % n) + 1

        if current == 1:
            break

    return ''.join(path)


n1, m1, n2, m2 = map(int, sys.argv[1:5])

result = get_path(n1, m1) + get_path(n2, m2)

print(result)