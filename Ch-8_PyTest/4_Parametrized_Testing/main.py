def weather_check(temp:float)->str:
    if temp>30:
        return "hot"
    elif temp<15:
        return "cold"
    else:
        return "moderate"
    
print(weather_check(35))