import os.path

import requests
import urllib3
from lxml import etree
from concurrent.futures import ThreadPoolExecutor
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def safe_filename(name):
    import re
    """移除不能用於檔名的字元"""
    return re.sub(r'[\\/*?:"<>|]', '_', name)

def make_headers(cookie_num):
    """
    將存放好的cookie文件逐個讀取, 並解析爲headers給requests
    cookie地址: ./cookies/
    cookie文件名格式: cookie{cookie_num}.txt , 注意:cookie_num從0開始

    :return: 一段headers
    """
    import json
    with open(f"/home/clydecole/Desktop/爬蟲代碼/use/1.溼熱爬取文章/cookies/cookies{cookie_num}.txt", "r") as f:
        cookies_list = json.load(f)
    cookie_str = "; ".join([f"{c['name']}={c['value']}" for c in cookies_list])
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/142.0.7444.59 Safari/537.36",
        "cookie": cookie_str
    }
    return headers

class GetContent:
    def __init__(self, fid, page):
        """
        初始設定

        :param fid: 就fid
        :param page: 頁面
        """
        self.main_url = "https://www.shireyishunjian.com/main/"
        self.target_url = f"{self.main_url}forum.php"
        self.headers = make_headers(0)
        self.params = {
            "mod" : "forumdisplay",
            "fid" : fid,
            "page": page
        }

    def get_title_and_href(self):
        """
        獲取文章標題和網頁鏈接

        :return: 標題和tid
        """
        import re
        resp = requests.get(self.target_url, params=self.params, verify=False)
        et = etree.HTML(resp.text)
        ths = et.xpath('//*[@id="threadlisttableid"]/tbody/tr/th[@class="new"]')

        title = []
        tid = []
        page = []

        for th in ths:

            href = th.xpath('./a[@class="s xst"]/@href')[0]
            if href: # tid
                tid.append(re.findall(r"tid=(.*?)&", href)[0])
            else:
                print("NO1")

            title.append(th.xpath('./a[@class="s xst"]/text()')[0]) # 標題

            pg = th.xpath('./span[@class="tps"]/a/text()')
            if pg:
                page.append(pg[len(pg) - 1]) # 頁面
            else:
                page.append(None)
        return title, tid, page

    def get_content(self, tid, page=None):
        """
        獲取內容

        :param tid: 就tid
        :param page: 總共擁有的個頁面
        :return: 使用者名稱列表, 評論時間列表, 評論內容列表
        """
        if page is None:
            page = 1

        def __get(params):
            html = requests.get(self.main_url + "forum.php", params=params, headers=self.headers, verify=False)
            et = etree.HTML(html.text)

            edt_time_list = []
            cmt_list = []

            user_name = et.xpath('//div/a[@class="xw1"]/text()')

            edit_time_em_list = et.xpath('//div[@class="pti"]/div/em')
            for edit_time_em in edit_time_em_list:
                if edit_time_em.xpath('./span'):
                    apd = edit_time_em.xpath('./span/@title')[0]
                    edt_time_list.append(apd)
                elif edit_time_em.xpath('./text()'):
                    apd = edit_time_em.xpath('./text()')[0]
                    edt_time_list.append(apd[4:])

            comments = et.xpath('//td[@class="t_f"]')
            for comment in comments:
                if comment.xpath('./div'):
                    reply = comment.xpath('./div/blockquote/text()')
                    if not reply[0].strip():
                        reply = comment.xpath('./div/blockquote/font[2]/text()')
                    cmt_list.append([reply, comment.xpath('./text()')])
                else:
                    cmt_list.append(comment.xpath('./text()'))

            return user_name, edt_time_list, cmt_list

        user_name_list = []
        edit_time_list = []
        comment_list = []
        # with ThreadPoolExecutor
        for pg in range(1, int(page) + 1):
            params = {
                "mod": "viewthread",
                "tid": tid,
                "extra": "page%3D1",
                "page": pg
            }

            user_name, edt_time_list, cmt_list = __get(params)
            user_name_list.append(user_name)
            edit_time_list.append(edt_time_list)
            comment_list.append(cmt_list)
        return user_name_list, edit_time_list, comment_list

    @staticmethod
    def write_files(tid, title, user_name, edit_time, comments):
        """

        :param title:
        :param tid:
        :param user_name:
        :param edit_time:
        :param comments:
        :return:
        """
        def __check_file():
            if os.path.exists("text.txt"):
                print(f"文件已經存在:text.txt")
                exit()

        title = safe_filename(title)
        with open(f"download/{tid}{title}.txt", 'a+') as f:
            for name, time, comment in zip(user_name, edit_time, comments):
                for a_name, a_time, a_comment in zip(name, time, comment):
                    if not isinstance(a_comment[0], list):
                        f.write(f"{a_time}  {a_name}\n"
                                f"comment:\n")
                        for c in a_comment:
                            if c.strip():
                                f.write(f"{c.strip()}\n")
                        f.write("\n\n")

                    else:
                        f.write(f"{a_time}  {a_name}\n"
                                f"reply:\n")
                        for c in a_comment[0]:
                            if c.strip():
                                f.write(f"{c.strip()}\n")
                        f.write(f"comment:\n")
                        for c in a_comment[1]:
                            if c.strip():
                                f.write(f"{c.strip()}\n")
                        f.write("\n\n")

        print("one time")



if __name__ == '__main__':
    get = GetContent(302, 1)
    title_lt, tid_lt, page_lt = get.get_title_and_href()
    print(title_lt)
    print(tid_lt)
    print(page_lt)

    def run(tid, title, page):
        user_name_list, edit_time_list, comment_list = get.get_content(tid, page)
        get.write_files(tid, title, user_name_list, edit_time_list, comment_list)

    with ThreadPoolExecutor(max_workers=36) as executor:
        for tid, title, page in zip(tid_lt, title_lt, page_lt):
            executor.submit(run, tid, title, page)
    print("all done")


