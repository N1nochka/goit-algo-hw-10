from pulp import *

# Створення змінних рішення
limonad = LpVariable("Лимонад", lowBound=0, cat='Integer')  # Кількість "Лимонаду"
fruit_juice = LpVariable("Фруктовий сік", lowBound=0, cat='Integer')  # Кількість "Фруктового соку"

# Створення задачі максимізації
prob = LpProblem("Максимізація виробництва", LpMaximize)

# Обмеження на кількість ресурсів
water_limit = 100
sugar_limit = 50
lemon_juice_limit = 30
fruit_puree_limit = 40

# Функція максимізації
prob += limonad + fruit_juice, "Загальна кількість продуктів"

# Обмеження на ресурси
prob += 2 * limonad + fruit_juice <= water_limit, "Вода"
prob += limonad <= sugar_limit, "Цукор"
prob += limonad <= lemon_juice_limit, "Лимонний сік"
prob += 2 * fruit_juice <= fruit_puree_limit, "Фруктове пюре"
prob += fruit_juice <= water_limit, "Вода для Фруктового соку"

# Вирішення задачі
prob.solve()

# Виведення результатів
print("Кількість 'Лимонаду':", value(limonad))
print("Кількість 'Фруктового соку':", value(fruit_juice))
