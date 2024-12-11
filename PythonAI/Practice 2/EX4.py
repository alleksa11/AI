def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def interpret_bmi(bmi):
    if bmi < 16:
        return "Выраженный дефицит массы тела"
    elif 16 <= bmi < 18.5:
        return "Недостат (дефицит) масса тела"
    elif 18.5 <= bmi < 25:
        return "Норма"
    elif 25 <= bmi < 30:
        return "Избыточная масса тела (предожирение)"
    elif 30 <= bmi < 35:
        return "Окирение 1 степени"
    elif 35 <= bmi < 40:
        return "Окирение 2 степени"
    else:
        return "Окирение 3 степени"

def main():
    # Запрос на ввод веса пользователя
    weight = float(input("Введите ваш вес в кг: "))

    # Запрос на ввод роста пользователя
    height = float(input("Введите ваш рост в метрах: "))

    # Вычисление ИМТ
    bmi = calculate_bmi(weight, height)

    # Интерпретация ИМТ
    interpretation = interpret_bmi(bmi)

    # Вывод результата
    print(f"Ваш ИМТ: {bmi:.2f}")
    print(f"Соответствие: {interpretation}")

    # Запрос на дальнейшие действия
    while True:
        action = input("Хотите ввести новые данные? (д/н): ").strip().lower()
        if action == "н":
            break
        elif action == "д":
            main()

if __name__ == "__main__":
    main()
