def divide_numbers():
    try:
        # Запрашиваем ввод двух чисел
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))

        # Проверяем, что второе число не равно нулю
        if num2 == 0:
            raise ZeroDivisionError("Деление на ноль невозможно!")

        # Выполняем деление
        result = num1 / num2
        print(f"Результат деления {num1} на {num2} равен: {result}")

    except ValueError:
        # Обрабатываем ошибку, если введено не число
        print("Ошибка: Вы ввели не число. Пожалуйста, введите числа.")

    except ZeroDivisionError as e:
        # Обрабатываем ошибку деления на ноль
        print(f"Ошибка: {e}")

    except Exception as e:
        # Обрабатываем любые другие исключения
        print(f"Произошла ошибка: {e}")


# Основной цикл программы
while True:
    divide_numbers()

    # Запрашиваем дальнейшие действия
    print("\nЧто вы хотите сделать дальше?")
    print("1. Попробовать снова")
    print("2. Выйти из программы")
    choice = input("Введите номер действия: ")

    if choice == "2":
        print("Выход из программы.")
        break