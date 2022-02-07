import api
import requests
from tools.get_logger import GetLogger

# 获取log日志器
log = GetLogger().get_logger()


class ApiGoods:
    # 1.初始化
    def __init__(self):
        # 商品详情接口url
        self.url_goods_detail = api.host + "/goods/v2/detail"
        log.info("正在初始化商品详情接口url：{}".format(self.url_goods_detail))
        # 商品价格计算接口url
        self.url_goods_price = api.host + "/goods/price"
        log.info("正在初始化商品价格计算接口url：{}".format(self.url_goods_price))
        # 商品搜索接口url
        self.url_goods_search = api.host + "/search/list"
        log.info("正在初始化商品搜索接口url：{}".format(self.url_goods_search))
        # 商品全部分类接口url
        self.url_goods_category = api.host + "/category/module_list"
        log.info("正在初始化商品分类接口url：{}".format(self.url_goods_category))
        # 商品分类列表接口url
        self.url_goods_category_list = api.host + "/category/goods"
        log.info("正在初始化商品分类列表接口url：{}".format(self.url_goods_category_list))

    # 商品详情接口
    def api_goods_detail(self, goodsId):
        # 定义请求数据
        data = {"goodsId": goodsId}
        log.info("正在调用商品详情接口，请求数据：{}".format(data))
        return requests.post(url=self.url_goods_detail, data=data, headers=api.headers)

    # 商品价格计算接口
    def api_goods_price(self, goodsId, number):
        # 定义请求数据
        data = {"goodsId": goodsId, "number": number}
        log.info("正在调用商品价格计算接口，请求数据：{}".format(data))
        return requests.post(url=self.url_goods_price, data=data, headers=api.headers)

    # 商品搜索接口
    def api_goods_search(self, keywords, page):
        # 定义请求数据
        data = {"keywords": keywords, "page": page}
        log.info("正在调用商品搜索接口，请求数据：{}".format(data))
        return requests.post(url=self.url_goods_search, data=data, headers=api.headers)

    # 商品全部分类接口
    def api_goods_category(self):
        log.info("正在调用全部商品分类接口")
        return requests.post(url=self.url_goods_category, headers=api.headers)

    # 商品分类列表接口
    def api_goods_category_list(self, catId, page):
        # 定义请求数据
        data = {"catId": catId, "page": page}
        log.info("正在调用商品分类列表接口，请求数据：{}".format(data))
        return requests.post(url=self.url_goods_category_list, data=data, headers=api.headers)