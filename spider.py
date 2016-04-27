# -*- coding: utf-8 -*-
import re
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class Spider:
    def __init__(self):
        print '开始抓取'
    def getSource(self,url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0'}
        html = requests.get(url,headers = headers)
        html.encoding = 'utf-8'
        return html.text
    def getAllurl(self,url,maxpage):
        allurl = []
        for i in range(1,maxpage+1):
            tempurl = re.sub('page=(\d+)','page=%d'%i,url,re.S)
            allurl.append(tempurl)
        return allurl
    def getAllSource(self,url,maxpage):
        allsource = []
        problem = []
        # for i in range(0,maxpage):
        html = self.getSource(url[1])
        temp = re.findall("<tr class='evenrow'>.*?</tr>|<tr class='oddrow'>.*?</tr>",html,re.S)
        print temp[1]
        a = re.findall('<nobr>(.*?)</nobr>',temp[1],re.S)
        print





