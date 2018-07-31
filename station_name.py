import requests

station_url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9061"

# 获取站点代码
page = requests.get(station_url)
stations = page.text[:-2].split('@')[1:]
# 格式
# 3字母缩写|站名|代码|拼音|拼音首字母缩写|序号
for s in stations:
    print(s)
