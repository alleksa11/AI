import matplotlib.pyplot
matplotlib.use('TkAgg')  # Или 'TkAgg'
import matplotlib.pyplot as plt

def main():
    # Запрос на ввод углового коэффициента и смещения
    m = float(input("Введите угловой коэффициент: "))
    b = float(input("Введите смещение: "))
    # Запрос на ввод диапазона значений по x
    x_min = float(input("Введите начальное значение x: "))
    x_max = float(input("Введите конечное значение x: "))
    x_step = float(input("Введите шаг изменения x: "))
    x_range = [x_min + i * x_step for i in range(int((x_max - x_min) / x_step) + 1)]
    # Генерация последовательности чисел (x, y)
    y_range = [m * x + b for x in x_range]
    # Построение графика
    plt.plot(x_range, y_range)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'График линейной функции y = {m}x + {b}')
    plt.grid(True)
    plt.show()

    # Запрос на дальнейшие действия
    while True:
        action = input("Хотите ввести новые данные? (д/н): ").strip().lower()
        if action == "н":
            break
        elif action == "д":
            main()

if __name__ == "__main__":
    main()
