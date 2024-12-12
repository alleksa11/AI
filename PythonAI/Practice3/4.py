import random
import matplotlib.pyplot as plt
import numpy as np

# Функция для вычисления MSE
def calculate_mse(source_data, k, b):
    mse = 0
    for x, y in source_data.items():
        predicted = k * x + b
        mse += (predicted - y) ** 2
    return mse / len(source_data)

# Функция для вычисления MAE
def calculate_mae(source_data, k, b):
    mae = 0
    for x, y in source_data.items():
        predicted = k * x + b
        mae += abs(predicted - y)
    return mae / len(source_data)

# Обучающая выборка
source_data = {
    22: 150,
    23: 155,
    24: 160,
    25: 162,
    26: 171,
    27: 174,
    28: 180,
    29: 183,
    30: 189,
    31: 192
}

# Инициализация случайных коэффициентов
k = random.uniform(-5, 5)
b = random.uniform(-5, 5)

print(f'Начальная прямая: Y = {k:.2f}*X + {b:.2f}')  # Вывод начальных значений

# Скорость обучения
rate = 0.0001

# Число итераций обучения
NUM_ITERS = 100000

# Обучение модели
for i in range(NUM_ITERS):
    x = random.choice(list(source_data.keys()))  # Случайная X-координата
    true_result = source_data[x]  # Соответствующая Y-координата
    out = k * x + b  # Ответ сети
    delta = true_result - out  # Ошибка сети
    k += delta * rate * x  # Корректировка веса k
    b += delta * rate  # Корректировка веса b

print(f'Обученная функция: Y = {k:.2f}*X + {b:.2f}')  # Вывод обученной функции

# Вычисление ошибок
mse = calculate_mse(source_data, k, b)
mae = calculate_mae(source_data, k, b)

print(f'Средняя абсолютная ошибка (MAE): {mae:.2f}')
print(f'Среднеквадратическая ошибка (MSE): {mse:.2f}')

# Построение графика
L = list(source_data.keys())
D = list(source_data.values())

X = []
Y = []
for x in range(min(L), max(L) + 1):
    y = k * x + b
    X.append(x)
    Y.append(y)

plt.plot(L, D, "r+", label='ИСХОДНЫЕ ДАННЫЕ')
plt.plot(X, Y, label=f'Обученная функция: y = {k:.2f}x + {b:.2f}')
plt.title('Зависимость прибыли от площади торгового павильона')
plt.xlabel('Площадь, м2')
plt.ylabel('Прибыль, млн. руб.', rotation=90)
plt.legend()
plt.show()