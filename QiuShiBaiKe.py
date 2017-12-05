import urllib.request
import urllib.parse
import http.cookiejar
import re

'''url = "https://www.zhihu.com/login/phone_num"
data = {
	"_xsrf": "32353036656463332d343062372d343032612d393862382d616663366633393164373265",
	"password": "TianTian562017",
	"captcha_type": "cn",
	"phone_num": "18302101720"
}
postdata = urllib.parse.urlencode(data).encode('utf-8')
req = urllib.request.Request(url, postdata)
req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4033.400 QQBrowser/9.6.12624.400")
cjar = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
file = opener.open(req)
data = file.read()
fhandle = open("G:/爬虫数据/1.html", "wb")
fhandle.write(data)
fhandle.close()
url2 = "https://www.zhihu.com/explore"
req2 = urllib.request.Request(url2, postdata)
req2.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4033.400 QQBrowser/9.6.12624.400")
data2 = urllib.request.urlopen(req2).read()
fhandle = open("G:/爬虫数据/2.html", "wb")
fhandle.write(data2)
fhandle.close()
'''


def getContent(url, i):
    # req = urllib.request.Request(url)
    # req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
    #                              "Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4033.400 QQBrowser/9.6.12624.400")
    headers = ("User-Agent", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                 "Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4033.400 QQBrowser/9.6.12624.400")
    opener = urllib.request.build_opener()
    opener.addheaders=[headers]
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(url).read().decode('utf-8')
    contentpat = '<div class="content">(.*?)</div>'
    contentlist = re.compile(contentpat, re.S).findall(data)
    x = 1
    for content in contentlist:
        print("第" + str(i) + "页的第" + str(x) + "个段子是：")
        pat1 = '<.*?>'
        content = re.sub(pat1, "", content)
        pat2 = '\n'
        content = re.sub(pat2, "", content)
        print(content)
        print("\n")
        x += 1

#i为想要下载的页数
for i in range(1, 3):
    url = "https://www.qiushibaike.com/8hr/page/" + str(i)
    getContent(url, i)
