import json, pprint
import re


def city_code_transfer(city_name: str) -> str or None:
    """
    :Args: 城市名
    :return: 存在返回那个城市的编号，反之 None
    """
    file = "/Users/momo/Desktop/Python_Auto/" \
           "第二部分/Chapter14/project/Data/citycode-2019-08-23.json"
    city_name = get_city_name(city_name)
    # print(city_name)
    with open(file) as f:
        jsonStrings = f.read()
        cityDics = json.loads(jsonStrings)
        for index, cityDic in enumerate(cityDics):
            # 如果用户输入的城市名存在，返回城市代码
            if city_name == cityDic["city_name"]:
                return cityDics[index]["city_code"]
    return None


def get_city_name(user_input: str) -> str:
    """
    我们 json 文件的数据城市名没有省还是市的，如果用户有输入的话，我们删除掉
    :arg:
        user_input，即用户输入的城市名字
    :return: 没有省或市的城市名
    """
    regex = re.compile(r'(\w+)(省|市$)')
    pure_city_name = regex.search(user_input)
    if pure_city_name is not None:
        # 只返回城市名，不要省｜市
        return pure_city_name.group(1)
    else:
        # 用户没有结尾省市的话，就原封不动返回
        return user_input


if __name__ == '__main__':
    code = city_code_transfer("浙江省")
    print(code)
