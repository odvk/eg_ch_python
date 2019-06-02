# найти периметр треугольника

# a = float(input("введите a:"))
# b = float(input("введите b:"))
# c = float(input("введите c:"))
#
# p = a + b + c
# print("Периметр =", p)

# ввод переменных в 1 строку
a, b, c = map(int, input("введите через пробел a b c: ").split())

p = a + b + c
print("Периметр =", p)
