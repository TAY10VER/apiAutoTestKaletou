from api.api_login import ApiLogin
from tools.tool import Tool
from parameterized import parameterized
from tools.get_logger import GetLogger
from tools.read_txt import read_txt

# 获取log日志器
log = GetLogger().get_logger()


def get_data():
    arrs = []
    for data in read_txt("login.txt"):
        arrs.append(tuple(data.strip().split(",")))
    return arrs[1:]


class TestLogin:
    # 初始化
    def setup_class(self):
        # 获取api对象
        self.login = ApiLogin()

    # 邮箱密码登录接口测试方法
    @parameterized.expand(get_data())
    def test01_login(self, username, pwd, code, msg, status):
        """登录接口测试"""
        try:
            # 判断是否正向用例
            if status == "true":
                try:
                    r = self.login.api_login(username, pwd)
                    # 打印结果
                    print("登录的结果为：", r.json())
                    # 提取token
                    Tool.common_token(r)
                    # 断言
                    Tool.common_assert(r, status_code=code, msg=msg)
                except Exception as e:
                    log.error(e)
            else:
                try:
                    r = self.login.api_login(username, pwd)
                    # 打印结果
                    print("登录的结果为：", r.json())
                    # 断言
                    Tool.common_assert(r, status_code=code, msg=msg)
                except Exception as e:
                    log.error(e)
        except Exception as e:
            log.error(e)

    # 电话密码登录测试方法
    def test02_login_phone(self, phone="17696640601", pwd="123456", nation_code="86"):
        """电话密码登录接口测试"""
        # 调用订单列表接口
        r = self.login.api_login_phone(phone, pwd, nation_code)
        print("登录结果：", r.json())
        # 断言
        try:
            Tool.common_assert(r, status_code="200", msg="登录成功")
        except Exception as e:
            log.error(e)

    # 手机号登录--发送验证码测试方法
    def test03_login_send_sms(self, nation_code="86", phone="17696640601"):
        """手机号登录--发送验证码接口测试"""
        # 调用手机号登录--发送验证码接口
        r = self.login.api_login_send_sms(nation_code, phone)
        print("登录验证码发送结果：", r.json())
        # 断言
        try:
            Tool.common_assert(r, status_code="200", msg="验证码发送成功")
        except Exception as e:
            log.error(e)