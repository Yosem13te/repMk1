# Запрос ИНН от пользователя
inn = input("Введите ИНН (12 цифр): ")

if len(inn) != 12 or not inn.isdigit():
    print("Некорректный ИНН. Он должен состоять из 12 цифр.")
else:
    # Преобразование строки в список цифр
    digits = list(map(int, inn))

    # Вектор коэффициентов для расчета контрольных цифр
    coefficients = [7, 2, 4, 10, 3, 5, 9, 4, 6, 8, 7, 3]

    # Расчет контрольных цифр с использованием вектора
    n11 = sum(digit * coefficient for digit, coefficient in zip(digits, coefficients)) % 11 % 10
    n12 = (3 * n11 + sum(digit * coefficient for digit, coefficient in zip(digits, coefficients[:10] + [8, n11]))) % 11 % 10

    # Проверка контрольных цифр
    if digits[10] == n11 and digits[11] == n12:
        print("ИНН корректен.")
        print(f"Код субъекта РФ: {inn[:2]}")
        print(f"Номер МНИ: {inn[2:4]}")
        print(f"Номер записи: {inn[4:10]}")
        print(f"1 контрольное число: {inn[10]}")
        print(f"2 контрольное число: {inn[11]}")
    else:
        print("Некорректный ИНН. Контрольные числа не совпадают.")"
