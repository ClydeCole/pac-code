import requests
from lxml import etree
xml = """
<book>
    <title>小源的奇妙冒險</title>
    <price currency="CNY">39.9</price>
    <tags>
        <tag type="genre">冒險</tag>
        <tag type="mood">熱血</tag>
    </tags>
    <author>
        <name id="a001">張三</name>
        <name id="a002">李四</name>
        <nickname class="cool">源仔</nickname>
        <div>
            <name>神秘人</name>
        </div>
    </author>
    <publisher>
        <name>幻想出版社</name>
        <address>北京朝陽區</address>
    </publisher>
</book>
"""

et = etree.XML(xml)
# result = et.xpath("/book") # 表示根節點
# result = et.xpath("/book/title/text()") # text() 拿文本
# result = et.xpath("/book/title/text()")[0]
# result = et.xpath("/book//name/text()") # // 表示所有的name
# result = et.xpath("/book/*/*/name/text()") # * 通配符
# result = et.xpath("/book/author/name[@id= 'a001']/text()") # [] 表示屬性篩選. @屬性= '值'    find(name, attrs={"id": "a001"})
# result = et.xpath("/book/tags/tag/@type") # 最後一個/ 表示拿到tag 裏的type 的屬性. @屬性. 可以直接拿到屬性值
# print(result)