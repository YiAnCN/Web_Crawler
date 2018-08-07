from demo01.mailTest import *
from demo01.weather import *
import time

if __name__ == '__main__':
    url="https://restapi.amap.com/v3/weather/weatherInfo?city=%E9%95%87%E6%B1%9F&output=json&key=1eae90276cd2adc12ac1212cc0cc8591"
    now_hour = time.strftime('%H', time.localtime(time.time()))
    send_time = int(now_hour)
    # print(send_time)
    while(True):
        if send_time == 22:
            weatherInformation = get_info(url)
            send_email(weatherInformation)
            print("已发送邮件")
            print("正在等待")
            time.sleep(60 * 60)
            print("过了一个小时")

        else:
            time.sleep(60 * 60)
            print("未到发送时间")