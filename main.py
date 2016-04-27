#coding=utf-8
from spider import *
maxpage = 20
url = 'http://acm.upc.edu.cn/problemset.php?page=1'
feng = Spider()
allurl = feng.getAllurl(url,maxpage)
feng.getAllSource(allurl,maxpage)

