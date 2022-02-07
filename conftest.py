import pytest
from py.xml import html
import api


def pytest_configure(config):
    # 添加接口地址和项目名称
    config._metadata["项目名称"] = "卡乐透接口自动化测试报告"
    config._metadata['接口地址'] = api.host
    # 删除Java_home
    config._metadata.pop("JAVA_HOME")


#添加summary内容
@pytest.mark.optionalhook
def pytest_html_results_summary(prefix):
    prefix.extend([html.p("所属部门: 测试组")])
    prefix.extend([html.p("测试人员: chenwanfeng")])


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('Description'))  # 表头添加Description
    cells.pop(-1)  # 删除link


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.td(report.description))  #表头对应的内容
    cells.pop(-1)  # 删除link列


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):  #description取值为用例说明__doc__
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)


# @pytest.mark.optionalhook
# def pytest_html_results_table_html(report, data):   #清除执行成功的用例logs
#     if report.passed:
#         del data[:]
#         data.append(html.div('用例pass展示的log.', class_='empty log'))

# class TestResult:
#     def __init__(self, outcome, report, logfile, config):
#         self.test_id = report.nodeid
#         if getattr(report, "when", "call") != "call":
#             self.test_id = "::".join([report.nodeid, report.when])
#         self.time = getattr(report, "duration", 0.0)
#         self.outcome = outcome
