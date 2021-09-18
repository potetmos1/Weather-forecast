from yr.libyr import Yr
import json
import datetime

weather = Yr(location_name='Norway/Oslo/Oslo/Oslo', forecast_link='forecast_hour_by_hour')

klokkeslett = datetime.datetime(1984,1,1,00,0,0)

for forecast in weather.forecast(str):
    data = json.loads(forecast)
    temp = data['temperature']
    rain = data['precipitation']
    regn = rain['@value']
    temperatur = temp['@value']
    if(klokkeslett.minute == 0):
        print(f"kl {klokkeslett.hour}:00 - {temperatur} - {regn}mm")
    else:
        print(f"kl {klokkeslett.hour}:{klokkeslett.minute} - {temperatur} - {regn}mm")

    klokkeslett = klokkeslett + datetime.timedelta(minutes=30)