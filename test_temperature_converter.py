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
