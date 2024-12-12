import matplotlib.pyplot as plt

# Пример словаря source_data
source_data = {
    10: 50,
    20: 80,
    30: 120,
    40: 150,
    50: 200
}

# Преобразование ключей и значений в списки
x_values = list(source_data.keys())  # Ключи (ось X)
y_values = list(source_data.values())  # Значения (ось Y)

# Построение точечного графика
plt.scatter(x_values, y_values, color='blue', label='Данные')
plt.xlabel('X (ключи словаря)')
plt.ylabel('Y (значения словаря)')
plt.title('Точечный график словаря source_data')
plt.grid(True)
plt.legend()
plt.show()