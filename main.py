from temperature_converter import TemperatureConverter


def main() -> None:
    converter = TemperatureConverter()
    print("Конвертер температур")
    print("1. Цельсий -> Фаренгейт")
    print("2. Фаренгейт -> Цельсий")
    print("3. Цельсий -> Кельвин")
    print("4. Кельвин -> Цельсий")
    choice = input("Выбери операцию (1-4): ")

    if choice not in ("1", "2", "3", "4"):
        print("Такой операции нет")
        return

    try:
        temperature = float(input("Введи температуру (дробная часть через точку): "))
        if choice == "1":
            result = converter.celsius_to_fahrenheit(temperature)
        elif choice == "2":
            result = converter.fahrenheit_to_celsius(temperature)
        elif choice == "3":
            result = converter.celsius_to_kelvin(temperature)
        else:
            result = converter.kelvin_to_celsius(temperature)
        print(f"Результат: {result:.2f}")
    except ValueError as error:
        print(f"Ошибка: {error}")


if __name__ == "__main__":
    main()
