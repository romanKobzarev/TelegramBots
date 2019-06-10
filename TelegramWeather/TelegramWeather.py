import pyowm

owm = pyowm.OWM('59bf42d6418c171f1581be4b8ef0ed9f', language="ru")
place = input("Какой город?:").strip()
try:
    observation = owm.weather_at_place(place)
    w = observation.get_weather()
    print(w)
except:
    print("""
    Города "{}" не существует
    Попробуйте другой город
    """ .format(place))

