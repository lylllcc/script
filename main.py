# -*- coding: utf-8 -*-
from spider import *
maxpage = 20
allline = []
url = 'http://acm.upc.edu.cn/problemset.php?page=1'
feng = Spider()
allurl = feng.getAllurl(url,maxpage)
for i in allurl:
    pagecode = feng.getSource(i) #获得当页源代码
    alllist = feng.getAlllist(pagecode) #获取当页所有资源
    print '当前获取 ' + i
    for j in alllist:
        line = feng.getLineSource(j)
        allline.append(line)
feng.write(allline)