import api
import requests
from tools.get_logger import GetLogger

# 获取log日志器
log = GetLogger().get_logger()


class ApiRegister:
    # 1.初始化
    def __init__(self):
        # 邮箱注册接口url
        self.url_register = api.host + "/user/register"
        log.info("正在初始化注册url：{}".format(self.url_register))
        # 手机注册--发送验证码接口url
        self.url_register_send_sms = api.host + "/user/reg_send_sms"
        log.info("正在初始化手机注册--发送验证码url：{}".format(self.url_register_send_sms))
        # 手机注册--验证验证码接口url
        self.url_register_check_sms = api.host + "/user/check_reg_sms"
        log.info("正在初始化手机注册--验证验证码url：{}".format(self.url_register_check_sms))

    # 邮箱注册接口
    def api_register(self, username, pwd, register_type):
        # 注册请求数据
        data = {
            "username": username,
            "password": pwd,
            "re_password": pwd,
            "type": register_type
        }
        log.info("正在调用注册接口，请求数据：{}".format(data))
        # 调用post方法
        return requests.post(url=self.url_register, data=data, headers=api.headers)

    # 手机注册——发送验证码接口
    def api_register_send_sms(self, nation_code, phone):
        # 注册发送验证码请求数据
        data = {
            "nation_code": nation_code,
            "phone": phone
        }
        log.info("正在调用手机注册——发送验证码接口，请求数据：{}".format(data))
        # 调用post方法
        return requests.post(url=self.url_register_send_sms, data=data, headers=api.headers)

    # 手机注册--验证验证码接口
    def api_register_check_sms(self, nation_code, phone, sms):
        data = {
            "nation_code": nation_code,
            "phone": phone,
            "sms": sms
        }
        log.info("正在调用手机注册--验证验证码接口，请求数据：{}".format(data))
        return requests.post(url=self.url_register_check_sms, data=data, headers=api.headers)