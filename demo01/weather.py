import requests
import json


def get_info(url):
    r =requests.get(url)
    result = r.text
    fin =json.loads(result)
    city = fin["lives"][0]["city"]
    weather = fin["lives"][0]["weather"]
    temperature = fin["lives"][0]["temperature"]
    winddirection = fin["lives"][0]["winddirection"]
    windpower = fin["lives"][0]["windpower"]
    humidity = fin["lives"][0]["humidity"]
    return "今天{0}的天气为{1}，温度为{2}，风向为{3}，风速为{4}级，湿度为{5}".format(city,weather,temperature,winddirection,windpower,humidity)
    # print(fin)
    # print(city)
    # print(weather)
    # print(temperature)
    # print(winddirection)
    # print(windpower)
    # print(humidity)