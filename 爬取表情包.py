import requests
from lxml import etree
import os
import threading


def get_url(url, img_urls): #获取图片url
    res = requests.get(url, headers=headers)    # 发送请求
    html = etree.HTML(res.text)     # 将html元素转换成html对象
    img_urls += html.xpath('//div[@class="thumbnail"]/a/img/@src')


def user_choose(): # 用户选择下载图片的页数
    img_urls = []  # 存放图片url
    # 请输入下载网址
    url = 'http://www.bbsnet.com/egao'
    # 用户输入页数
    page = int(input('请输入获取的页数：'))
    for i in range(0, page):
        if page == 0:
            get_url(url, img_urls)
        elif page >= 1:
            link = url + f'/page/{i+1}'     # 拼接链接
            get_url(link, img_urls)   #调用获取图片url的函数
    return img_urls


def download_picture(img_url, i, j): # 下载图片
    res = requests.get(img_url, headers)
    with open(f'./表情包/表情包-{i}.{j}', 'wb') as f:
        f.write(res.content)


if __name__ == '__main__':
    if not os.path.exists('./表情包'):
        os.makedirs('./表情包')

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }
    img_urls = user_choose()

    threads = []
    for i in range(len(img_urls)):
        t = threading.Thread(target=download_picture, args=(img_urls[i], i, img_urls[i][-3:]))
        threads.append(t)
    for t in threads:
        t.start()

