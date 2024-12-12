import matplotlib.pyplot as plt
import numpy as np


def linear_function(k, b, x):
    """Линейная функция: y = kx + b"""
    return k * x + b


def quadratic_function(a, b, c, x):
    """Квадратичная функция: y = ax^2 + bx + c"""
    return a * x ** 2 + b * x + c


def exponential_function(a, b, x):
    """Экспоненциальная функция: y = a * e^(b*x)"""
    return a * np.exp(b * x)


def get_user_input():
    """Запрашивает у пользователя тип функции и параметры."""
    print("Выберите тип функции:")
    print("1. Линейная функция (y = kx + b)")
    print("2. Квадратичная функция (y = ax^2 + bx + c)")
    print("3. Экспоненциальная функция (y = a * e^(b*x))")

    choice = int(input("Введите номер функции: "))

    if choice == 1:
        k = float(input("Введите угловой коэффициент k: "))
        b = float(input("Введите смещение b: "))
        return "linear", {"k": k, "b": b}
    elif choice == 2:
        a = float(input("Введите коэффициент a: "))
        b = float(input("Введите коэффициент b: "))
        c = float(input("Введите коэффициент c: "))
        return "quadratic", {"a": a, "b": b, "c": c}
    elif choice == 3:
        a = float(input("Введите коэффициент a: "))
        b = float(input("Введите коэффициент b: "))
        return "exponential", {"a": a, "b": b}
    else:
        print("Неверный выбор. Попробуйте снова.")
        return get_user_input()


def plot_function(function_type, params, x_range):
    """Построение графика функции."""
    x = np.linspace(x_range[0], x_range[1], 1000)

    if function_type == "linear":
        y = linear_function(params["k"], params["b"], x)
    elif function_type == "quadratic":
        y = quadratic_function(params["a"], params["b"], params["c"], x)
    elif function_type == "exponential":
        y = exponential_function(params["a"], params["b"], x)

    plt.plot(x, y, label=f"{function_type} function")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(f"График {function_type} функции")
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    while True:
        # Запрашиваем тип функции и параметры
        function_type, params = get_user_input()

        # Запрашиваем диапазон значений по x
        x_start = float(input("Введите начальное значение x: "))
        x_end = float(input("Введите конечное значение x: "))
        x_range = (x_start, x_end)

        # Строим график
        plot_function(function_type, params, x_range)

        # Запрашиваем дальнейшие действия
        print("Что вы хотите сделать дальше?")
        print("1. Ввести новые данные")
        print("2. Выйти из программы")
        next_action = input("Введите номер действия: ")

        if next_action == "2":
            print("Выход из программы.")
            break


if __name__ == "__main__":
    main()