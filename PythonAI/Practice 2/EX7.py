# # Задаем номер варианта (N)
# N = 25  # Замените на ваш номер варианта
# N_squared = N ** 2
#
# # Список для хранения введенных значений x
# x_values = []
#
# # Цикл для ввода 7 значений x
# for i in range(7):
#     while True:
#         try:
#             x = float(input(f"Введите значение x ({i+1}/7): "))
#             if x > N_squared:
#                 print(f"Введенное число больше {N_squared}. Повторите ввод.")
#             else:
#                 x_values.append(x)
#                 break
#         except ValueError:
#             print("Ошибка: введите числовое значение.")
#
# # Вычисление значений функции y = 3x^2 + 6x + 9
# y_values = []
# for x in x_values:
#     y = 3 * x**2 + 6 * x + 9
#     y_values.append(y)
#
# # Вывод результатов
# print("\nРезультаты вычислений:")
# for i in range(len(x_values)):
#     print(f"x = {x_values[i]}, y = {y_values[i]}









# Определение номера варианта (N)
N = 25  # Замените на ваш номер варианта
N_squared = N ** 2

# Генерация 7 значений x с помощью функции range()
x_values = list(range(1, 8))  # Значения x от 1 до 7

# Вычисление значений функции y = 3x^2 + 6x + 9
y_values = []
for x in x_values:
    y = 3 * x**2 + 6 * x + 9
    y_values.append(y)

# Вывод результатов
print("\nРезультаты вычислений:")
for i in range(len(x_values)):
    print(f"x = {x_values[i]}, y = {y_values[i]}")