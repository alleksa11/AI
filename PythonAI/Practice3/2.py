import matplotlib.pyplot as plt


def linear_function(k, b, x):
    """Вычисляет значение линейной функции y = kx + b для заданного x."""
    return k * x + b


def main():
    # Запрашиваем у пользователя коэффициенты линейной функции
    k = float(input("Введите коэффициент k (угловой коэффициент): "))
    b = float(input("Введите коэффициент b (смещение): "))

    # Запрашиваем диапазон значений и шаг
    x_start = float(input("Введите начальное значение x: "))
    x_end = float(input("Введите конечное значение x: "))
    step = float(input("Введите шаг: "))

    # Проверяем корректность диапазона и шага
    if x_start >= x_end or step <= 0:
        print("Ошибка: Некорректный диапазон или шаг. Убедитесь, что x_start < x_end и step > 0.")
        return

    # Формируем списки значений аргументов и функции
    x_values = []
    y_values = []
    x = x_start

    while x <= x_end:
        y = linear_function(k, b, x)
        x_values.append(x)
        y_values.append(y)
        x += step

    # Выводим списки на экран
    print("\nЗначения аргументов (x):", x_values)
    print("Значения функции (y):", y_values)

    # Строим график функции
    plt.plot(x_values, y_values, label=f"y = {k}x + {b}", color="blue")
    plt.scatter(x_values, y_values, color="red", label="Точки (x, y)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("График линейной функции")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()