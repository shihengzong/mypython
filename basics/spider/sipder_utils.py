# -*- coding: UTF-8 -*-
import sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import urllib.request as url_req
import urllib.parse as parse
import re
from myos import myos
import public_var  

# 获取网站内容
def open_url(url):
    req = url_req.Request(url)
    req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36")
    res = url_req.urlopen(req)
    html = res.read().decode("utf-8")
    # print(html)
    return html

# 'img src="" attr="36103" data-original="https://imgsa.baidu.com/forum/wh%3D200%2C90%3B/sign=5703a70054b5c9ea62a60be1e5099a39/1a6722600c3387448860be775e0fd9f9d62aa0dc.jpg'

def get_img(html):
    p = r'<img src="" .+bpic="(.+\.jpg)"'
    # p = r'<img src="".+data-original="(.+\.jpg)'
    result = re.findall(p,html)
    # 遍历图片
    str = ""
    for v in result:
        # str += (v+"\n") 
        file_name = v.split("/")[-1]
        url_req.urlretrieve(v,public_var.spider_dir+public_var.jiandi_dir+file_name,None) # urlretrieve 下载方法
    # return str



# 主程启动
if __name__ == "__main__":
    url = "https://tieba.baidu.com/f?kw=dnf%E5%89%91%E5%B8%9D"
    html = open_url(url)
    result = get_img(html)
    # 生成文件
    # write_result = myos.saveFile(public_var.spider_dir,public_var.tieba_jiandi,result)
    # if write_result == 0:
    #     print("写入失败")
    # else:
    #     print("写入成功")
    



