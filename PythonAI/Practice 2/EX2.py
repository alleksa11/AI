import datetime

def calculate_age(year_of_birth):
    current_year = 2024
    age = current_year - year_of_birth
    return age

def main():
    # Запрос на ввод имени пользователя
    name = input("Введите ваше имя: ")

    # Запрос на ввод года рождения пользователя
    year_of_birth = int(input("Введите ваш год рождения: "))

    # Вычисление возраста пользователя
    age = calculate_age(year_of_birth)

    # Вывод результата
    print(f"Ваш возраст: {age} лет")

    # Запрос на дальнейшие действия
    while True:
        action = input("Хотите ввести новые данные? (д/н): ").strip().lower()
        if action == "н":
            break
        elif action == "д":
            main()

if __name__ == "__main__":
    main()
