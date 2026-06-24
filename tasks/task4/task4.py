import sys


with open(sys.argv[1], "r") as f:
    nums = [int(line.strip()) for line in f if line.strip()]

nums.sort()
median = nums[len(nums) // 2]

moves = sum(abs(num - median) for num in nums)

if moves <= 20:
    print(moves)
else:
    print(
        "20 ходов недостаточно для приведения всех элементов массива к одному числу"
    )