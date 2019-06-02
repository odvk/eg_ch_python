# ввод переменных в 1 строку
# https://informatics.msk.ru/mod/statements/view3.php?id=3309&chapterid=3466
a, b, l, N = map(float, input("введите через пробел a b l N: ").split())

# вариант 1
# L = 2*l+(2*a*(N-1)+a) + 2*b*(N-1)

# вариант 2. преобразованная формула
L = a + 2 * (l + (N - 1) * (a + b))

print("Периметр =", L)
