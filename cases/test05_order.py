from api.api_order import ApiOrder
from tools.tool import Tool
from parameterized import parameterized
from tools.read_txt import read_txt
from tools.get_logger import GetLogger

# 获取log日志器
log = GetLogger().get_logger()

# 订单详情测试数据
def get_data():
    arrs = []
    for data in read_txt("order_sn.txt"):
        arrs.append(tuple(data.strip().split(",")))
    return arrs[1:]


class TestOrder:
    # 初始化
    def setup_class(self):
        # 获取api_order对象
        self.order = ApiOrder()

    # 订单列表接口测试方法
    def test01_order_list(self, status="all"):
        """
        订单列表接口测试
        :param status: 1.全部订单：all  2.未付款订单：unpaid  3.待发货订单：unshipped  4.已完成订单：completed
        """
        # 调用订单列表接口
        r = self.order.api_order_list(status)
        print("订单列表数据为：", r.json())
        # 断言
        try:
            Tool.common_assert(r, status_code="200", msg="成功")
        except Exception as e:
            log.error(e)

    # 订单详情接口测试方法
    @parameterized.expand(get_data())
    def test02_order_detail(self, order_sn, code, msg):
        """订单详情接口测试"""
        # 调用订单详情接口
        r = self.order.api_order_detail(order_sn)
        print("订单详情数据为：", r.json())
        # 断言
        try:
            Tool.common_assert(r, status_code=code, msg=msg)
        except Exception as e:
            log.error(e)

    # 添加购物车测试方法
    goods_input = '[{"name":"sdoname","value":"ceshi"}]'

    def test03_order_addcart(self, goodsId="1430", number="1", input=goods_input):
        """添加购物车接口测试"""
        # 调用添加购物车接口
        r = self.order.api_order_add_cart(goodsId, number, input)
        print("添加购物车返回数据数据为：", r.json())
        # 断言
        try:
            Tool.common_assert(r, status_code="200", msg="成功")
        except Exception as e:
            log.error(e)

    # checkout测试方法
    def test04_order_checkout(self, pay_Id="5", bonus_Id="0"):
        """checkout接口测试"""
        # 调用checkout接口
        r = self.order.api_order_checkout(pay_Id=pay_Id, bonus_Id=bonus_Id)
        print("checkout接口返回数据数据为：", r.json())
        # 断言
        try:
            Tool.common_assert(r, status_code="200", msg="成功")
        except Exception as e:
            log.error(e)

    # 生成订单接口测试方法
    def test05_order_paydone(self, pay_Id="5", bonus_Id="0", usesurplus="0"):
        """生成订单接口测试"""
        # 调用生成订单接口
        r = self.order.api_order_paydone(pay_Id=pay_Id,bonus_Id=bonus_Id,usesurplus=usesurplus)
        print("生成订单接口返回数据数据为：", r.json())
        # 断言
        try:
            Tool.common_assert(r, status_code="200", msg="成功")
        except Exception as e:
            log.error(e)