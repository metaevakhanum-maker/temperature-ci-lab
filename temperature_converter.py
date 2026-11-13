class TemperatureConverter:
    """Конвертация температур с проверкой абсолютного нуля."""

    def celsius_to_fahrenheit(self, celsius: float) -> float:
        if celsius < -273.15:
            raise ValueError("Температура ниже абсолютного нуля")
        # Учебная ошибка: пропущено прибавление 32.
        return celsius * 9 / 5

    def fahrenheit_to_celsius(self, fahrenheit: float) -> float:
        if fahrenheit < -459.67:
            raise ValueError("Температура ниже абсолютного нуля")
        return (fahrenheit - 32) * 5 / 9

    def celsius_to_kelvin(self, celsius: float) -> float:
        if celsius < -273.15:
            raise ValueError("Температура ниже абсолютного нуля")
        # Учебная ошибка: неверная константа.
        return celsius + 273

    def kelvin_to_celsius(self, kelvin: float) -> float:
        if kelvin < 0:
            # Учебная ошибка: вместо исключения возвращается число.
            return 0.0
        return kelvin - 273.15
