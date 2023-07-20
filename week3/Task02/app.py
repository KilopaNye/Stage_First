import bs4
import urllib.request as req
import csv


#進入文章讀取Po文時間，並return抓取到的時間資料。
def getTime(TimeUrl):
    requests = req.Request(
        TimeUrl,
        headers={
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36"
        },
    )
    with req.urlopen(requests) as response:
        data = response.read().decode("utf-8")
#解析html文件
    TimeRoot = bs4.BeautifulSoup(data, "html.parser")
    shareTimeBox = TimeRoot.find_all("span", class_="article-meta-value")
    return  shareTimeBox[3].string


def getPage(url):
    with open("attraction.csv", mode="a", newline="", encoding="utf-8") as attraction:
        writer = csv.writer(attraction)
        request = req.Request(
            url,
            headers={
                "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36"
            },
        )
        with req.urlopen(request) as response:
            data = response.read().decode("utf-8")

        root = bs4.BeautifulSoup(data, "html.parser")
        titles = root.find_all("div", class_="title")
        nums = root.find_all("div", class_="nrec")
        for i in range(len(titles)):
            if titles[i].a != None and titles[i].a["href"] != "/bbs/movie/M.1630756788.A.1FE.html":
                Sharetime = getTime("https://www.ptt.cc"+titles[i].a["href"])
                
                if nums[i].span ==None:
                    result= titles[i].a.string,"0",Sharetime
                    writer.writerow(result)
                else:
                    result = titles[i].a.string,nums[i].span.string,Sharetime
                    writer.writerow(result)

        nextLink = root.find("a", string="‹ 上頁")
        return nextLink["href"]


pageUrl = "https://www.ptt.cc/bbs/movie/index.html"
count=0
while count<3:
    pageUrl ="https://www.ptt.cc"+getPage(pageUrl)
    count+=1


