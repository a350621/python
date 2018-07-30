#作業
# 1.使用台北市公開資料的[台北市台北旅遊網-景點資料] 
# 2.使用者可以用捷運站名稱搜尋景點
# 3.將對應到的景點資訊，處存在檔案中
import urllib.request as request
import json #處理JSON資料格式 (JavaScript Object Notation)
with request.urlopen("http://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=36847f3f-deff-4183-a5bb-800737591de5")as response:
    data=json.load(response)

keyword=input("搜尋捷運站名稱： ")
list=data["result"]["results"]
n=0
with open("data.txt", "w", encoding="utf-8") as file:
    for info in list:
        if info["MRT"]==keyword:
            file.write(info["stitle"]+"\n")
            n=n+1
    if n>0:
        print("已存入")
    else:
        print("沒有推薦的景點")