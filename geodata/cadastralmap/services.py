import time
import folium
import json
from rosreestr2coord import Area


def get_map(cadastral_number):
    # таймер времнеи выполнения скрипта
    start = time.time()

    # получение географических данных с помощью кадастрового номера
    area = Area(cadastral_number) 
    data = json.loads(area.to_geojson_poly())
    
    if data:
        # получение центра области для отображения карты
        x = data['properties']['center'].get('x')
        y = data['properties']['center'].get('y')

        # получение карты для отображения на html странице
        m = folium.Map(location=[y , x], zoom_start=17)
        folium.GeoJson(data, name="geojson").add_to(m)
        m=m._repr_html_() 

        # запись врекмени выоплнения
        result = time.time() - start
        result = '{:.2e}'.format(result) if result < 1 else round(result, 2)

        return {'result': result, 'map': m}
    else:
        return {'error': 'Не удалось загрузить карту по кадастровому номеру'}