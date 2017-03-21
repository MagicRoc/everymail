import sys

KEY = 'jdyqwv0dak023ypl'  # API key
UID = "U6BC9FDBA7"  # 用户ID

LOCATION = 'nanyang'  # 所查询的位置，可以使用城市拼音、v3 ID、经纬度等
API = 'https://api.thinkpage.cn/v3/weather/now.json'  # API URL，可替换为其他 URL
UNIT = 'c'  # 单位
LANGUAGE = 'zh-Hans'  # 查询结果的返回语言


def getLocation():
    """get location from user input
    default beijing
    """
    argvs = sys.argv
    location = argvs[1] if len(argvs) >= 2 else LOCATION
    return location
