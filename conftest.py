# -*- coding: utf-8 -*-
# @Time    : 2023/2/15 15:31
# @Author  : WuBingTai
import time

from config import *
import pytest
from driver import get_driver, get_web_driver
from loguru import logger


@pytest.fixture()
def driver_setup(request):
    request.instance.ip = driver_ip
    request.instance.driver = get_driver(driver_ip)
    logger.info("driver初始化")
    request.instance.driver.app_start(page_name, stop=True)
    time.sleep(lanuch_time)
    allow(request.instance.driver)

    def driver_teardown():
        logger.info("自动化测试结束!")
        request.instance.driver.watcher.stop()
        request.instance.driver.app_stop(page_name)

    request.addfinalizer(driver_teardown)

    time.sleep(3)


# Chromedriver方式使用这个
@pytest.fixture()
def web_driver_setup(request):
    request.instance.driver = get_driver(driver_ip)
    logger.info("driver初始化")
    request.instance.driver.app_start(page_name, stop=True)
    time.sleep(lanuch_time)
    allow(request.instance.driver)
    logger.info("web_driver初始化")
    request.instance.web_driver = get_web_driver(request.instance.driver, driver_ip + port)

    # allow(request.instance.driver)
    def driver_teardown():
        logger.info("自动化测试结束!")
        request.instance.web_driver.quit()
        request.instance.driver.watcher.stop()
        request.instance.driver.app_stop(page_name)

    request.addfinalizer(driver_teardown)
    time.sleep(3)


def allow(driver):
    driver.watcher.when('//*[@text="拒绝"]').when('//*[@text="允许"]').click()
    driver.watcher.when('//*[@content-desc="温馨提示"]').when('//*[@content-desc="同意"]').click()
    driver.watcher.when('//*[@content-desc="立即更新"]').when('//*[@content-desc="下次再说"]').click()
