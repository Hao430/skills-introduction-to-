import requests
from concurrent.futures import ThreadPoolExecutor
import re
# 导入必要的库
f = open("host.txt", "w")# 打开一个名为"host.txt"的文件以写入模式


def get_ip(url):# 定义一个函数，用于获取指定URL的IP地址
    resp = requests.get(url)# 使用requests库发送GET请求到指定的URL
    status = resp.status_code# 获取响应的状态码
    if status == 200: # 如果状态码为200，表示请求成功
        f.write(url + "\n") # 将URL写入到"host.txt"文件中
        print(url)# 打印URL到控制台


url = []# 创建一个列表，包含从1到254的数字，每个数字后面都跟着一个URL格式
for i in range(1, 255):# 使用线程池执行器，最多使用100个工作线程来并行执行get_ip函数
    url.append("http://192-168-1-" + str(i) + ".pvp3696.bugku.cn")#“网址”
with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(get_ip, url)