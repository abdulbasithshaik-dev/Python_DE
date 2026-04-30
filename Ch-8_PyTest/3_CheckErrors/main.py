class weather:


    def weather_check(self,temp:float)->str:
        if  temp<0:
            return "It's freezing outside"
        elif temp<15:
            return "It's a bit chilly"
        elif temp<25:
            return "The Weather is pleasant"
        else:
            return "It's hot outside!"
        
    def rain_chance(self,rain_chance:float)->str:
        if rain_chance>0.7:
            return "High chance of rain, carry an umbrella!"
        elif rain_chance>0.4:
            return "Moderate chance of rain, be prepared!"
        else:
            return "Low chance of rain, enjoy your day!"
        
    def divide(self,a:float,b:float)->float:
        if b==0:
            raise ValueError("Cannot divide by zero")
        return a/b