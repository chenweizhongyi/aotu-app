import os
from public.Operate import Operate
from public.BaseOperate import BaseOperate
from public.logger import Logger
# yamlpath = os.path.dirname(os.path.dirname(os.path.abspath('.'))) + '\\testyaml\\cm\\cm-001tkclick.yaml'
# print(yamlpath)
logger = Logger('test_click_age').logger
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
yamlpath = PATH("../../testyaml/cm/cm-001tkclick.yaml")
# print(yamlpath)
class TestClickAge:

    def __init__(self,driver):
        self.path = yamlpath
        self.driver = driver
        self.operate = Operate(self.path,self.driver)
        self.base = BaseOperate(self.driver)

    def clickage(self):
        self.base.swipe_up()
        self.operate.check_operate_type()
        logger.info('购买成功')
        self.base.screenshot()
        # assert

    def home(self):
        self.operate.back_home()

# from public.GetDriver import mydriver
# x = TestClickAge(driver=mydriver())
# x.clickage()