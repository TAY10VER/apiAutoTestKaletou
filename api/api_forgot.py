import api
import requests
from tools.get_logger import GetLogger

# 获取log日志器
log = GetLogger().get_logger()


class ApiForgot:
    # 1.初始化
    def __init__(self):
        # 手机忘记密码接口url
        self.url_find_pwd_phone = api.host + "/user/find_pwd_phone"
        log.info("正在初始化手机忘记密码接口url：{}".format(self.url_find_pwd_phone))
        # 邮箱忘记密码--发送验证码接口url
        self.url_email_get_code = api.host + "/email/get_code"
        log.info("正在初始化邮箱忘记密码--发送验证码接口url：{}".format(self.url_email_get_code))
        # 邮箱忘记密码--验证验证码接口url
        self.url_email_check_code = api.host + "/user/forgot"
        log.info("正在初始化邮箱忘记密码--验证验证码接口url：{}".format(self.url_email_check_code))

    # 手机忘记密码接口
    def api_forgot_find_pwd_phone(self, nation_code, phone):
        # 定义请求数据
        data = {"nation_code": nation_code, "phone": phone}
        log.info("正在调用手机忘记密码接口，请求数据：{}".format(data))
        return requests.post(url=self.url_find_pwd_phone, data=data, headers=api.headers)

    # 邮箱忘记密码--发送验证码接口
    def api_forgot_email_get_code(self, email):
        # 定义请求数据
        data = {"email": email}
        log.info("正在调用邮箱忘记密码--发送验证码接口，请求数据：{}".format(data))
        return requests.post(url=self.url_email_get_code, data=data, headers=api.headers)

    # 邮箱忘记密码--发送验证码接口
    def api_forgot_email_check_code(self, email, v_code):
        # 定义请求数据
        data = {"email": email, "v_code": v_code}
        log.info("正在调用邮箱忘记密码--验证验证码接口，请求数据：{}".format(data))
        return requests.post(url=self.url_email_check_code, data=data, headers=api.headers)
