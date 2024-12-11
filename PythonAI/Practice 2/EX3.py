weight = float(input("Масса тела в кг:"))
height = float(input("Рост в метрах:"))
bmi = weight / (height**2)
print(f"Ваш ИМТ: {bmi:.2f}")
