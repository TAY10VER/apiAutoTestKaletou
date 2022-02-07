import api
import requests
from tools.get_logger import GetLogger

# 获取log日志器
log = GetLogger().get_logger()


class ApiLogin:
    # 1.初始化
    def __init__(self):
        # 邮箱/用户名登录接口url
        self.url_login = api.host + "/user/login"
        log.info("正在初始化邮箱/用户名登录接口url：{}".format(self.url_login))
        # 电话密码登录接口url
        self.url_login_phone = api.host + "/user/login_phone"
        log.info("正在初始化电话密码登录接口url：{}".format(self.url_login_phone))
        # 手机号登录--发送验证码接口url
        self.url_login_send_sms = api.host + "/user/login_send_sms"
        log.info("正在初始化手机号登录--发送验证码接口url：{}".format(self.url_login_send_sms))

    # 邮箱登录接口
    def api_login(self, username, pwd):
        # 定义请求数据
        data = {"username": username, "password": pwd}
        log.info("正在调用登录接口，请求数据：{}".format(data))
        return requests.post(url=self.url_login, data=data, headers=api.headers)

    # 电话密码登录接口
    def api_login_phone(self, phone, pwd, nation_code):
        # 定义请求数据
        data = {"phone": phone, "password": pwd, "nation_code":nation_code}
        log.info("正在调用电话密码登录接口，请求数据：{}".format(data))
        return requests.post(url=self.url_login_phone, data=data, headers=api.headers)

    # 手机号登录--发送验证码接口
    def api_login_send_sms(self, nation_code, phone):
        # 定义请求数据
        data = {"nation_code": nation_code, "phone": phone}
        log.info("正在调用登录-发送验证码接口，请求数据：{}".format(data))
        return requests.post(url=self.url_login_send_sms, data=data, headers=api.headers)
