import re
from bs4 import BeautifulSoup

s = """
<div class='西遊記'><span id='10010'>中國聯通</span></div>
<div class='西遊記'><span id='10086'>中國移動</span></div>
"""

obj = re.compile(r"<span id='(?P<id>\d+)'>(?P<name>.*?)</span>")
result = obj.finditer(s)
for item in result:
    id = item.group("id")
    print(id)
    name = item.group("name")
    print(name)