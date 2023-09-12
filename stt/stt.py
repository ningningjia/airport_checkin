import json
import requests
import time


def login(auth_url: str, email: str, passwd: str):
    login_header = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41",
        "x-requested-with": "XMLHttpRequest",
        "origin": "https://stt.lol",
        "referer": "https://stt.lol/auth/login"}
    form_data = {"email": email, "passwd": passwd, "remember_me": "on", "code": ""}
    r = requests.post(url=auth_url, headers=login_header, data=form_data)
    r.close()
    print(get_time(), json.loads(r.content))
    str_cookie = "lang=zh-cn"
    for i in r.cookies.items():
        str_cookie = str_cookie+'; '+i[0]+'='+i[1]
    return str_cookie


def checkin(checkin_url: str, cookies: str):
    checkin_header = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41",
        "x-requested-with": "XMLHttpRequest",
        "origin": "https://stt.lol",
        "referer": "https://stt.lol/user",
        "cookie": cookies}

    r = requests.post(checkin_url, headers=checkin_header)
    r.close()
    print(get_time(), json.loads(r.content))


def get_time():
    now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return now_time


if __name__ == '__main__':
    with open("./stt/config.json", 'r') as f:
        config = json.load(f)
    print("{}配置文件为".format(get_time()), config)
    cookie = login(auth_url=config["login_url"], email=config["email"], passwd=config["passwd"])
    print("{}获取的Cookie为".format(get_time()), cookie)
    checkin(checkin_url=config["checkin_url"], cookies=cookie)