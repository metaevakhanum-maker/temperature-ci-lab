class TemperatureConverter:
    """Конвертация температур с проверкой абсолютного нуля."""

    def celsius_to_fahrenheit(self, celsius: float) -> float:
        if celsius < -273.15:
            raise ValueError("Температура ниже абсолютного нуля")
        return celsius * 9 / 5 + 32

    def fahrenheit_to_celsius(self, fahrenheit: float) -> float:
        if fahrenheit < -459.67:
            raise ValueError("Температура ниже абсолютного нуля")
        return (fahrenheit - 32) * 5 / 9

    def celsius_to_kelvin(self, celsius: float) -> float:
        if celsius < -273.15:
            raise ValueError("Температура ниже абсолютного нуля")
        return celsius + 273.15

    def kelvin_to_celsius(self, kelvin: float) -> float:
        if kelvin < 0:
            raise ValueError("Температура ниже абсолютного нуля")
        return kelvin - 273.15
