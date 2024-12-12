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


# Функция для обучения модели
def train_model(source_data, rate, num_iters):
    k = random.uniform(-5, 5)
    b = random.uniform(-5, 5)

    for i in range(num_iters):
        x = random.choice(list(source_data.keys()))  # Случайная X-координата
        true_result = source_data[x]  # Соответствующая Y-координата
        out = k * x + b  # Ответ сети
        delta = true_result - out  # Ошибка сети
        k += delta * rate * x  # Корректировка веса k
        b += delta * rate  # Корректировка веса b

    return k, b


# Варьирование параметров
rates = [0.00001, 0.0001, 0.001]
num_iters_list = [100000, 1000000, 10000000]

# Таблица для хранения результатов
results = []

# Проведение экспериментов
for rate in rates:
    for num_iters in num_iters_list:
        k, b = train_model(source_data, rate, num_iters)
        mse = calculate_mse(source_data, k, b)
        results.append((rate, num_iters, k, b, mse))

# Вывод результатов
print("Результаты экспериментов:")
print("| Скорость обучения (rate) | Число итераций (NUM_ITERS) | k | b | MSE |")
for result in results:
    print(f"| {result[0]:.5f} | {result[1]:10} | {result[2]:.5f} | {result[3]:.5f} | {result[4]:.5f} |")

# Построение графика для последнего эксперимента
k, b = results[-1][2], results[-1][3]
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