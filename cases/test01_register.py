import time
from api.api_register import ApiRegister
from tools.tool import Tool
from parameterized import parameterized
from tools.get_logger import GetLogger
from tools.read_txt import read_txt
import pytest

# 获取log日志器
log = GetLogger().get_logger()


def get_data():
    arrs = []
    for data in read_txt("register.txt"):
        arrs.append(tuple(data.strip().split(",")))
    return arrs[1:]


class TestRegister:
    # 初始化
    def setup_class(self):
        # 获取api对象
        self.register = ApiRegister()

    # 邮箱注册失败测试方法
    @parameterized.expand(get_data())
    def test01_register_failed(self, username, pwd, register_type, code, msg):
        """注册失败测试方法"""
        try:
            r = self.register.api_register(username, pwd, register_type)
            # 打印结果
            print("注册结果为：", r.json())
            # 断言
            Tool.common_assert(r, status_code=code, msg=msg)
        except Exception as e:
            log.error(e)

    # 邮箱注册成功测试方法
    # register_email = ''.join(random.sample('123efer45dsfer678dd9abcdef', 8)) + "@kacn.com"
    register_email = time.strftime("%Y-%m-%d_%H%M%S", time.localtime()) + "@kacn.com"
    # @pytest.mark.skip(reason="link注册接口邮件存在问题，暂不执行此用例")
    def test02_register_success(self, register_email=register_email, pwd="111111", register_type="email"):
        """注册成功接口测试"""
        r = self.register.api_register(register_email, pwd, register_type)
        print("注册结果为：", r.json())
        try:
            Tool.common_assert(r, status_code="200", msg="注册成功")
        except Exception as e:
            log.error(e)

    # 手机注册——发送验证码接口测试方法
    def test03_register_send_sms(self, nation_code="86", phone="17696640601"):
        """手机注册--发送验证码接口测试"""
        r = self.register.api_register_send_sms(nation_code, phone)
        print("注册验证码发送结果：", r.json())
        # 断言
        try:
            Tool.common_assert(r, status_code="600029", msg="电话已存在")
        except Exception as e:
            log.error(e)

    # 手机注册--验证验证码接口测试方法
    def test04_register_check_sms(self):
        pass
