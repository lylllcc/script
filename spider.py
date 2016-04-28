#coding:utf-8
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
    def getAlllist(self,html):
        return re.findall("<tr class='evenrow'>.*?</tr>|<tr class='oddrow'>.*?</tr>",html,re.S)
    def getLineSource(self,str):
        tempprobelmid = re.search("<div class='center'>(.*?)</div>", str, re.S).group(1)
        tempproblem = re.search("<a href='problem[.]php[?]id=(\d+)'>(.*?)</a>", str, re.S).group(2)
        tempac = re.search("jresult=(\d+)'>(.*?)</a>", str, re.S).group(2)
        tempsub = re.search("<a href='status.php[?]problem_id=(\d+)'>(.*?)</a>", str, re.S).group(2)
        temp = {}  # 暂时存放放一个问题 人数的列表
        temp['problemid'] = tempprobelmid
        temp['problem'] = tempproblem
        temp['ac'] = tempac
        temp['sub'] = tempsub
        return temp
    def write(self,allline):
        f = open('date.txt','w')
        for each in allline:
            f.writelines("Problem ID: "+each['problemid']+"  Problem: " + each['problem']+"  提交人数: "+each['sub']+"  AC人数: "+each['ac']+"\n")
        f.close()
        print "写入成功"