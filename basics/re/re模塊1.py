import re
import requests

headers = {
    "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
}
pages = 0
for i in range(0,221,20):


    data = {
        "type": "17",
        "interval_id": "100:90",
        "action": "",
        "start": f"{i}",
        "limit": "20"
    }

    url = "https://movie.douban.com/j/chart/top_list"
    pages += 1
    print("######################")
    print(f"pages{pages}")
    resp = requests.get(url, params=data, headers=headers)

    text = str(resp.json())
    result = re.finditer("'title': '(.*?)', 'url'", text) # 每次for 循環的時候都會加載正則表達式
    for w in result:
        print(w.group(1))


# # 預加載，，提前把正則對象加載完畢
# obj = re.compile("'title': '(.*?)', 'url'")# 創建obj
# for item in xxx:
#     obj.finditer(item)


    # text = str(resp.json())
    # obj = re.compile("'title': '(.*?)', 'url'")
    # for item in obj.finditer(text):
    #     print(item.group(1))
