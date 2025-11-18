import requests
from lxml import etree

html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <title>Title</title>
</head>
<body>
    <ul>
        <li><a href="http://www.baidu.com">百度</a></li>
        <li><a href="http://www.google.com">谷歌</a></li>
        <li><a href="http://www.sogou.com">搜狗</a></li>
    </ul>
    <ol>
        <li><a href="feiji">飞机</a></li>
        <li><a href="dapao">大炮</a></li>
        <li><a href="huoche">火车</a></li>
    </ol>
    <div class="job">李嘉诚</div>
    <div class="common">胡辣汤</div>
</body>
</html>
"""


et = etree.HTML(html)
# li_list = et.xpath("/html/body/ul/li[2]/a/text()") 
# print(li_list)
# li_list = et.xpath("/html/body/ul/li/a/@href")
# name_list = et.xpath("/html/body/ul/li/a/text()")
# print(li_list, name_list)

li_list = et.xpath("//li")
for li in li_list:
    herf = li.xpath("./a/@href")[0]
    text = li.xpath("./a/text()")[0]
    print(text, herf)
requests.get("","")