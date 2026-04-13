import requests
from pprint import pprint

# 문제4. C번의 데이터를 활용하여, 섭씨 온도 데이터를 추가합니다.


def get_result(api_key):
    
    # 요구사항에 맞도록 이곳의 코드를 수정합니다.
    to_korean = {
        'feels_like' : '체감온도',
        'humidity' : '습도',
        'pressure' : '기압',
        'temp' : '온도',
        'temp_max' : '최고온도',
        'temp_min' : '최저온도',
        'description' : '요약',
        'icon' : '아이콘',
        'main' : '핵심',
        'id' : '식별자',
        'weather':'날씨',
        'grnd_level':'지표면기압',
        'sea_level':'해수면기압',
    }    

    url = f'https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid={api_key}'
    response = requests.get(url).json()
    

    # 데이터 가공
    main_data, weather_data ={}, {}
    for key,value in response['main'].items():
        main_data[to_korean[key]] = value
        # 온도가 포함되어 있다면 데이터 가공 후 추가하기
        if '온도' in to_korean[key]:
            main_data[to_korean[key] + '(섭씨)'] = round(value - 273.15 ,2)

    for key, value in response['weather'][0].items():
        weather_data[to_korean[key]] = value
    result = {
        to_korean['main'] : main_data,
        to_korean['weather'] : [weather_data],
    }

    return result

# 여러분의 OpenWeatherMap API 키를 설정하세요

# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_result(api_key)
    # prrint.prrint(): json 을 보기 좋은 형식으로 출력
    pprint(result)