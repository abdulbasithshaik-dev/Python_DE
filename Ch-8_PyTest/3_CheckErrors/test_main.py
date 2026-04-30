from main import weather
import pytest
#test cases for weather_check function
def test_weather_check():
    w=weather()
    assert w.weather_check(-5)=="It's freezing outside"
    assert w.weather_check(10)=="It's a bit chilly"
    assert w.weather_check(20)=="The Weather is pleasant"
    assert w.weather_check(35)=="It's hot outside!"


def test_rain_chance():
    w=weather()
    assert w.rain_chance(0.8)=="High chance of rain, carry an umbrella!"
    assert w.rain_chance(0.5)=="Moderate chance of rain, be prepared!"
    assert w.rain_chance(0.2)=="Low chance of rain, enjoy your day!"

def test_divide():
    w=weather()
    assert w.divide(10,2)==5
    assert w.divide(9,3)==3
    
    with pytest.raises(ValueError,match="Cannot divide by zero"):
        w.divide(10,0)