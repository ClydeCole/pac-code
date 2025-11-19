def make_headers(cookie_num):
    import json
    """
    將存放好的cookie文件逐個讀取, 並解析爲headers給requests
    cookie地址: ./cookies/
    cookie文件名格式: cookie{cookie_num}.txt , 注意:cookie_num從0開始

    :return: 一段headers
    """
    with open(f"./cookies/cookies{cookie_num}.txt", "r") as f:
        cookies_list = json.load(f)
    cookie_str = "; ".join([f"{c['name']}={c['value']}" for c in cookies_list])
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/142.0.7444.59 Safari/537.36",
        "cookie": cookie_str
    }
    return headers