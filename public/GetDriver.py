# coding=utf-8
# author='Shichao-Dong'

import time
from appium import webdriver
from selenium.common.exceptions import WebDriverException
# from public.readConfig import Readconfig
from public.readConfig import Readconfig
# import public.GetDevices
from public.GetDevices import devices
from public.StartAppiumServer import Sp
# from logs import log
import json
# log = log()
conf = Readconfig()
cmd = devices()


deviceName = cmd.get_deviceName()
platformVersion = cmd.get_platformVersion().encode('ascii')
platformName = conf.getConfigValue('platformName')
appPackage = conf.getConfigValue('appPackage').encode('ascii')
appActivity = conf.getConfigValue('appActivity').encode('ascii')

s = Sp(deviceName)
appium_port = s.main()

# class MyEncoder(json.JSONEncoder):
#
#     def default(self, obj):
#         """
#         只要检查到了是bytes类型的数据就把它转为str类型
#         :param obj:
#         :return:
#         """
#         if isinstance(obj, bytes):
#             return str(obj, encoding='utf-8')
#         return json.JSONEncoder.default(self, obj)
# x = MyEncoder()

def mydriver():

    #desired_caps = {}
    # desired_caps['platformName'] = 'Android'  # 设备系统
    # desired_caps['platformVersion'] = '7.1.2'  # 设备系统版本
    # desired_caps['deviceName'] = 'vivo-9x'  # 设备名称
    # # desired_caps['app'] = os_path + '\\app\\e7594d12d6e485c6f812a8a0a0d870d2.apk'
    # # desired_caps['noReset'] = True
    # desired_caps['appPackage'] = 'com.tiankun.xian'
    # desired_caps['appActivity'] = 'com.uzmap.pkg.EntranceActivity'
    #
    # driver = webdriver.Remote('http://127.0.0.1:%s/wd/hub' %str(appium_port), desired_caps)
    # return driver
    desired_caps = {}
    desired_caps['platformName'] = platformName  # 设备系统
    desired_caps['platformVersion'] = '7.1.2'  # 设备系统版本
    desired_caps['deviceName'] = deviceName  # 设备名称
    # desired_caps['app'] = os_path + '\\app\\e7594d12d6e485c6f812a8a0a0d870d2.apk'
    # desired_caps['noReset'] = True
    desired_caps['appPackage'] = 'com.tiankun.xian'
    desired_caps['appActivity'] = 'com.uzmap.pkg.EntranceActivity'
                # 'platformName':platformName,'deviceName':deviceName, 'platformVersion':platformVersion,
                # 'appPackage':appPackage,'appActivity':appActivity,
                # 'unicodeKeyboard':True,'resetKeyboard':True,'noReset':True,
                # 'newCommandTimeout':180
    print(desired_caps)
    try:
        driver = webdriver.Remote('http://127.0.0.1:%s/wd/hub' %str(appium_port), desired_caps)
        # print(type(driver))
        time.sleep(4)
        # log.info('获取driver成功')
        return driver
    except WebDriverException:
        print ('No driver')




if __name__ == "__main__":

    mydriver()