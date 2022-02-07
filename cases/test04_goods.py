from api.api_goods import ApiGoods
from tools.tool import Tool
from tools.get_logger import GetLogger

# 获取log日志器
log = GetLogger().get_logger()


class TestGoods:
    # 初始化
    def setup_class(self):
        # 获取api_goods对象
        self.goods = ApiGoods()

    # 商品详情接口测试方法
    def test01_goods_detail(self, goodsId="1430"):
        """商品详情接口测试"""
        # 调用商品详情接口
        r = self.goods.api_goods_detail(goodsId)
        print("商品详情数据为：", r.json())
        # 断言
        try:
            Tool.common_assert(r, status_code="200", msg="成功")
        except Exception as e:
            log.error(e)

    # 商品价格计算接口测试方法
    def test02_goods_price(self, goodsId="1430", number = "2"):
        """商品价格计算接口测试"""
        # 调用商品价格计算接口
        r = self.goods.api_goods_price(goodsId, number)
        print("商品价格数据为：", r.json())
        # 断言
        try:
            Tool.common_assert(r, status_code="200", msg="成功")
        except Exception as e:
            log.error(e)

    # 商品搜索接口测试方法
    def test03_goods_search(self, keywords="代购", page="1"):
        """商品搜索接口测试"""
        # 调用商品搜索接口
        r = self.goods.api_goods_search(keywords, page)
        print("商品搜索数据为：", r.json())
        # 断言
        try:
            Tool.common_assert(r, status_code="200", msg="成功")
        except Exception as e:
            log.error(e)

    # 商品全部分类测试方法
    def test04_goods_category(self):
        """全部商品分类接口测试"""
        # 调用商品全部分类接口
        r = self.goods.api_goods_category()
        print("商品全部分类数据为：", r.json())
        # 断言
        try:
            Tool.common_assert(r, status_code="200", msg="成功")
        except Exception as e:
            log.error(e)

    # 商品分类列表接口测试方法
    def test05_goods_category_list(self, catId="527", page = "1"):
        """商品分类列表接口测试"""
        # 调用商品分类列表接口
        r = self.goods.api_goods_category_list(catId, page)
        print("商品分类列表数据为：", r.json())
        # 断言
        try:
            Tool.common_assert(r, status_code="200", msg="成功")
        except Exception as e:
            log.error(e)