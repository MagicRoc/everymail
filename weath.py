import json
import sys
import re
import requests
from weath_value import API, KEY, UNIT, LANGUAGE, getLocation


def fetchWeather():
    """通过API获取天气信息"""

    location = getLocation()
    result = requests.get(API, params={
        'key': KEY,
        'location': location,
        'language': LANGUAGE,
        'unit': UNIT
    }, timeout=100)
    values = json.loads(result.text)
    results = values["results"][0]
    wea = results["now"]
    time = re.sub(r'([\d|-]+)T([\d|:]+).+', r'\1 \2', results["last_update"])
    return wea,time


if __name__ == '__main__':
    wea,time = fetchWeather()
    print(wea,time)
