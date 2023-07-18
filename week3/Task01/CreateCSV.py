import json, urllib.request
import csv

url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
# ----------------------- attraction資料抓取並寫入-------------------------
with open("attraction.csv", mode="w", newline="", encoding="utf-8") as attraction:
    writer = csv.writer(attraction)
    with urllib.request.urlopen(url) as json_data:
        # 將JSON進行UTF-8的BOM解碼，並把解碼後的資料載入JSON陣列中
        data = json.loads(json_data.read().decode("utf-8-sig"))
    # 指定內文為result
    result = data["result"]["results"]
    for i in range(len(result)):
        # 篩選出第一筆圖片網址
        first_url = result[i]["file"].split("https://")
        # 景點名稱,區域,經度,緯度,第⼀張圖檔網址
        write_in = (
            result[i]["stitle"],
            result[i]["address"][4:8],
            result[i]["longitude"],
            result[i]["latitude"],
            "https://" + first_url[1],
        )
        # 寫入資料
        writer.writerow(write_in)

# ------------------------MRT所需資料製作-------------------------------------
with open("mrt.csv", mode="w", newline="", encoding="utf-8") as mrt:
    writer = csv.writer(mrt)
    with urllib.request.urlopen(url) as json_data:
        # 將JSON進行UTF-8的BOM解碼，並把解碼後的資料載入JSON陣列中
        data = json.loads(json_data.read().decode("utf-8-sig"))
    # 指定內文為result
    result = data["result"]["results"]
    for i in range(len(result)):
        write_in = result[i]["MRT"], result[i]["stitle"]
        # 寫入資料
        writer.writerow(write_in)

# ------------------------MRT讀取資料整理並寫入------------------------------
with open("mrt.csv", mode="r", newline="", encoding="utf-8") as mrt:
    writer = csv.reader(mrt)
    writer = list(writer)
    writer.sort(key=lambda x: x[0])
    with open("mrt.csv", mode="w", newline="", encoding="utf-8") as mrt:
        data = csv.writer(mrt)
        answer = ()
        # 這邊使用tuple的+=功能進行長度增加 假如站名與前一個不相符則加入站名title 反之增加景點名稱至tuple中
        # 假如再執行一次加入站名title的功能，則先印入資料一次當作斷點，並繼續下一站的輪播。以此類推
        for i in range(len(writer)):
            # 將沒有捷運站的景點剔除
            if bool(writer[i][0]) != False:
                if writer[i][0] != writer[i - 1][0]:
                    if len(answer) >= 1:
                        data.writerow(answer)
                    answer = writer[i][0], writer[i][1]
                else:
                    answer += (writer[i][1],)
