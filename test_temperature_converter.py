import pytest

from temperature_converter import TemperatureConverter


@pytest.fixture
def converter():
    return TemperatureConverter()


def test_celsius_to_fahrenheit(converter):
    assert converter.celsius_to_fahrenheit(0.0) == pytest.approx(32.0)


def test_fahrenheit_to_celsius(converter):
    assert converter.fahrenheit_to_celsius(212.0) == pytest.approx(100.0)


def test_celsius_to_kelvin(converter):
    assert converter.celsius_to_kelvin(0.0) == pytest.approx(273.15)


def test_kelvin_to_celsius(converter):
    assert converter.kelvin_to_celsius(273.15) == pytest.approx(0.0)


def test_negative_kelvin(converter):
    with pytest.raises(ValueError):
        converter.kelvin_to_celsius(-1.0)


@pytest.mark.parametrize(
    "celsius, fahrenheit, kelvin",
    [
        (-273.15, -459.67, 0.0),
        (-40.0, -40.0, 233.15),
        (0.0, 32.0, 273.15),
        (36.6, 97.88, 309.75),
        (100.0, 212.0, 373.15),
    ],
)
def test_conversion_cases(converter, celsius, fahrenheit, kelvin):
    assert converter.celsius_to_fahrenheit(celsius) == pytest.approx(fahrenheit)
    assert converter.fahrenheit_to_celsius(fahrenheit) == pytest.approx(celsius)
    assert converter.celsius_to_kelvin(celsius) == pytest.approx(kelvin)
    assert converter.kelvin_to_celsius(kelvin) == pytest.approx(celsius)


@pytest.mark.parametrize(
    "celsius, fahrenheit, kelvin",
    [
        (-273.16, -459.68, -0.01),
        (-300.0, -500.0, -10.0),
    ],
)
def test_invalid_temperatures(converter, celsius, fahrenheit, kelvin):
    with pytest.raises(ValueError):
        converter.celsius_to_fahrenheit(celsius)
    with pytest.raises(ValueError):
        converter.fahrenheit_to_celsius(fahrenheit)
    with pytest.raises(ValueError):
        converter.celsius_to_kelvin(celsius)
    with pytest.raises(ValueError):
        converter.kelvin_to_celsius(kelvin)
