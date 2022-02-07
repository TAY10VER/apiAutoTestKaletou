import api
import requests
from tools.get_logger import GetLogger

# 获取log日志器
log = GetLogger().get_logger()


class ApiOrder:
    # 1.初始化
    def __init__(self):
        # 订单列表接口url
        self.url_order_list = api.host + "/order/list"
        log.info("正在初始化订单列表url：{}".format(self.url_order_list))
        # 订单详情接口url
        self.url_order_detail = api.host + "/order/detail"
        log.info("正在初始化订单详情url：{}".format(self.url_order_detail))
        # 添加购物车url
        self.url_add_cart = api.host + "/flow/addCart"
        log.info("正在初始化添加购物车url：{}".format(self.url_add_cart))
        # checkout url
        self.url_checkout = api.host + "/flow/checkOut"
        log.info("正在初始化checkout url：{}".format(self.url_checkout))
        # 生成订单url
        self.url_pay_done = api.host + "/flow/payDone"
        log.info("正在初始化生产订单 url：{}".format(self.url_pay_done))

    # 订单列表接口
    def api_order_list(self, status):
        # 请求数据
        data = {"page": "", "page_size": "", "status": status}
        log.info("正在调用订单列表接口，请求数据：{}".format(data))
        # 调用post方法
        return requests.post(url=self.url_order_list, data=data, headers=api.headers)

    # 订单详情接口
    def api_order_detail(self, order_sn):
        # 请求数据
        data = {"order_sn": order_sn}
        log.info("正在调用订单列表接口，请求数据：{}".format(data))
        # 调用post方法
        return requests.post(url=self.url_order_detail, data=data, headers=api.headers)

    # 添加购物车接口
    def api_order_add_cart(self, goodsId, number, goods_input):
        # 请求数据
        data = {"goodsId": goodsId, "number": number, "goodsInput": goods_input}
        log.info("正在调用添加购物车接口，请求数据：{}".format(data))
        # 调用post方法
        return requests.post(url=self.url_add_cart, data=data, headers=api.headers)

    # checkout 接口
    def api_order_checkout(self, pay_Id, bonus_Id):
        # 请求数据
        data = {"payId": pay_Id, "bonusId": bonus_Id}
        log.info("正在调用checkout接口，请求数据：{}".format(data))
        # 调用post方法
        return requests.post(url=self.url_checkout, data=data, headers=api.headers)

    # 生成订单 接口
    def api_order_paydone(self, pay_Id, bonus_Id, usesurplus):
        # 请求数据
        data = {"payId": pay_Id, "bonusId": bonus_Id, "useSurplus": usesurplus}
        log.info("正在调用生成订单接口，请求数据：{}".format(data))
        # 调用post方法
        return requests.post(url=self.url_pay_done, data=data, headers=api.headers)