from spider import *
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
if __name__ == '__main__':
url = 'http://www.jikexueyuan.com/course/?pageNum=1'
myspider = Spider()
all_links = mySpider.changePage(url,20)
for link in all_links:
    print "正在处理页面" + link
    html = myspider.getSource(url)
    everyclass = myspider.getEveryclass(html)







