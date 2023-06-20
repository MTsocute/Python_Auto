#! python3
from location_code_transfer import *
import sys, requests, json
import pprint

# 检测用户输入是否正确【解决没有输入地址这个参数的问题】
if len(sys.argv) != 2:
    print(f'你没有输入参数哦！\n   使用方法：quickWeather.py [你想知道天气的城市名]')
    sys.exit()
elif not sys.argv[1].isalpha():
    sys.exit(f'请你检查下你输入的是不是城市名嘞')

# 如果没有退出就说明，用户输入了一个城市名
location = sys.argv[1]

# 获取城市代码
city_code = city_code_transfer(location)
# 有些省份可能没有城市代码（不能查天气）
if city_code is None:
    print(f'{location} 无法字节获取天气，请通过其网页查询!')
    sys.exit()

# 获取城市天气信息的API请求
url = f"http://t.weather.itboy.net/api/weather/city/{city_code}"

# 检测是否请求到内容，请求失败会报错 404
try:
    # 返回 response 对象
    response = requests.get(url)
    response.raise_for_status()
except Exception as err:
    print(f'{err}')
else:
    weather_dic = json.loads(response.text)
    pprint.pprint(weather_dic['data'])
