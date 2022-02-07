import api
from tools.get_logger import GetLogger

# 获取log日志器
log = GetLogger().get_logger()


class Tool:

    @classmethod
    def common_token(cls, response):
        # 提取token
        token = response.json().get("data").get("token")
        # 追加到请求headers中
        api.headers["token"] = token
        log.info("正在提取token，提取后的header为：{}".format(api.headers))
        print("添加token后的headers为：", api.headers)

    @classmethod
    def common_assert(cls, response, status_code, msg):
        """
        :param response: 请求相应对象
        :param status_code: 预期相应状态码
        :param msg: 预期相应信息msg
        """
        # 断言状态码
        log.info("正在断言状态码，预期状态码：{}，实际相应状态码：{}".format(status_code, response.json().get("code")))
        assert status_code == str(response.json().get("code"))
        log.info("正在断言响应信息，预期msg：{}，实际相应msg：{}".format(msg, response.json().get("msg")))
        assert msg == response.json().get("msg")
