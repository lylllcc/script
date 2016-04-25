#coding=utf-8
import re
import requests

#设置编码
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Spider:
    def __init__(self):
        print '开始抓取。。。。'
    #获取网页源代码
    def getSource(self,url):
        header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0'}
        html = requests.get(url,header = header)
        html.encoding = 'utf-8'
        return html.text
    def changPage(self,url,max_page):
        now_page = int(re.search('pageNum=(\d+)',url,re.S).group(1))
        page_group = []
        for i in range(now_page,max_page+1):
            link = re.sub('pageNum=(\d+)','pageNum=%d'%i,url,re.S)
            page_group.append(link)
        return page_group
    def getEveryclass(self,url):



