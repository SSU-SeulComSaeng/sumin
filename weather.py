def get_weather() : 
    import requests
    import json
    from PIL import Image

    apikey = "8445902c451c8a09a6c9c0ee6966b798"
    city = "Seoul"

    api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}"

    result = requests.get(api)
    data = json.loads(result.text)

    # 온도를 켈빈에서 섭씨로 변환
    temp_kelvin = data["main"]["temp"]
    temp_celsius = int(round(temp_kelvin - 273.15, 1))
    
    return(temp_celsius, data["weather"][0]["main"], data["name"])


weather_data = get_weather()

print("Temperature:", weather_data[0])
print("Weather:", weather_data[1])
print("City:", weather_data[2])

