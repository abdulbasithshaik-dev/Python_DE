from main import weather_check
import pytest

@pytest.mark.parametrize("temp,expected",[
    (-5, "cold"),
    (10, "cold"),
    (20, "moderate")
])

def test_weather_check(temp, expected):
    assert weather_check(temp) == expected
    assert weather_check(35)=="hot"


if __name__=="__main__":
    test_weather_check()
