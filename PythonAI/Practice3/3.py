import matplotlib.pyplot as plt

# Исходный словарь: ключи - площади торговых павильонов, значения - приносимый доход
data = {
    50: 12000,
    75: 18000,
    100: 25000,
    120: 30000,
    150: 36000
}

# Преобразование ключей (площади) в список
areas = list(data.keys())

# Преобразование значений (доходы) в список
incomes = list(data.values())

# Вывод массивов данных
print("Площади торговых павильонов:", areas)
print("Приносимый доход:", incomes)

# Построение графика
plt.plot(areas, incomes, marker='o', linestyle='-', color='blue', label='Доход от площади')
plt.scatter(areas, incomes, color='red', label='Точки данных')
plt.xlabel('Площадь, м²')
plt.ylabel('Доход, руб.')
plt.title('Зависимость дохода от площади торгового павильона')
plt.grid(True)
plt.legend()
plt.show()