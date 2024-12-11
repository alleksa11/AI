while True:
    try:
        b = float(input("Введите длину стороны квадрата: "))
        if b > 0:
            area = b ** 2
            perimeter = 4 * b
            print("Площадь квадрата:",area)
            print("Периметр квадрата:",perimeter)

            if area > 100:
                print("Площадь квадрата больше 100!")
            if perimeter > 50:
                print("Периметр квадрата больше 50!")
            else:
                print("Периметр квадрата меньше 50.")
        else:
            print("Ошибка: длина стороны должна быть положительным числом.")
    except ValueError:
        print("Ошибка: длина стороны должна быть числом.")
