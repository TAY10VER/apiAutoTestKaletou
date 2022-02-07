from api.api_forgot import ApiForgot
from tools.tool import Tool
from parameterized import parameterized
from tools.get_logger import GetLogger
from tools.read_txt import read_txt

# 获取log日志器
log = GetLogger().get_logger()


# 手机忘记密码测试数据
def get_data1():
    arrs = []
    for data in read_txt("find_pwd_phone.txt"):
        arrs.append(tuple(data.strip().split(",")))
    return arrs[1:]


# 邮箱忘记密码测试数据
def get_data2():
    arrs = []
    for data in read_txt("find_pwd_email.txt"):
        arrs.append(tuple(data.strip().split(",")))
    return arrs[1:]


class TestForgot:
    # 初始化
    def setup_class(self):
        # 获取api_forgot对象
        self.forgot = ApiForgot()

    @parameterized.expand(get_data1())
    def test01_forgot_find_pwd_phone(self, nation_code, phone, code, msg):
        """手机忘记密码接口测试"""
        r = self.forgot.api_forgot_find_pwd_phone(nation_code, phone)
        print("手机忘记密码接口返回结果：", r.json())
        # 断言
        try:
            Tool.common_assert(r, status_code=code, msg=msg)
        except Exception as e:
            log.error(e)

    @parameterized.expand(get_data2())
    def test02_forgot_find_pwd_email(self, email, code, msg):
        """手机忘记密码--发送验证码接口测试"""
        r = self.forgot.api_forgot_email_get_code(email)
        print("邮箱忘记密码--发送验证码接口返回结构", r.json())
        # 断言
        try:
            Tool.common_assert(r, status_code=code, msg=msg)
        except Exception as e:
            log.error(e)

    def test03_forgot_email_check_code(self, email="chenwanfeng@kacn.com", v_code="111111"):
        """手机忘记密码--验证验证码"""
        r = self.forgot.api_forgot_email_check_code(email,v_code)
        print("邮箱忘记密码--验证验证码接口返回结构", r.json())
        # 断言
        try:
            Tool.common_assert(r, status_code="600044", msg="验证码错误")
        except Exception as e:
            log.error(e)