import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа
n = 1000  # Кількість випадкових точок

# Генеруємо випадкові значення x
x_values = np.random.uniform(a, b, n)

# Обчислюємо значення функції для кожного випадкового x
y_values = f(x_values)

# Оцінка площі під кривою
area_mc = (b - a) * np.mean(y_values)

# Обчислення інтеграла за допомогою функції quad
result_quad, _ = spi.quad(f, a, b)

# Визначення похибки
error = abs(area_mc - result_quad)

# Виведення результатів
print("Площа під кривою методом Монте-Карло:", area_mc)
print("Інтеграл, обчислений за допомогою функції quad:", result_quad)
print("Похибка:", error)

# Побудова графіка
x = np.linspace(a, b, 1000)
y = f(x)

plt.plot(x, y, 'r', label='f(x) = x^2')  # Графік функції
plt.fill_between(x, y, color='gray', alpha=0.3)  # Заповнення області під кривою
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Метод Монте-Карло для обчислення інтеграла')
plt.legend()
plt.grid(True)

plt.show()