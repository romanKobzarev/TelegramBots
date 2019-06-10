import pyowm

owm = pyowm.OWM('59bf42d6418c171f1581be4b8ef0ed9f', language="ru")
place = input("Какой город?:").strip()
try:
    observation = owm.weather_at_place(place)
    w = observation.get_weather()
except:
    print("""
    Города "{}" не существует
    Попробуйте другой город
    """.format(place))
print("""В городе {City} сейчас {Status}""".format(City=place, Status=w.get_detailed_status()))
print('''Температура сейчас равна {}'''.format(w.get_temperature('celsius')['temp']))
if w.get_temperature('celsius')['temp'] <= 10:
    print('Сейчас очень холодно. Надень шапку!')
elif w.get_temperature('celsius')['temp'] <= 20:
    print('Сейчас прохладно, лучше надеть куртку.')
else: print('Сейчас на улице тепло. Можешь бегать в шортиках и футболке :)')