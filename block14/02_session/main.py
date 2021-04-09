print("Введите первую точку")
x1 = float(input('X: '))
y1 = float(input('Y: '))
print("\nВведите вторую точку")
x2 = float(input('X: '))
y2 = float(input('Y: '))

k = y1 - y2
b = x2 - x1

print("Уравнение прямой, проходящей через эти точки:")
print("y = ", k, " * x + ", b)