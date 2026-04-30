from main import weather_check

#test cases for weather_check function

def test_weather_check():
    assert weather_check(-5)=="cold"
    assert weather_check(10)=="cold"
    assert weather_check(20)=="moderate"
    assert weather_check(35)=="hot"


if __name__=="__main__":
    test_weather_check()
