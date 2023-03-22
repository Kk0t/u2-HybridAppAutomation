# -*- coding: utf-8 -*-
# @Time    : 2023/2/7 15:03
# @Author  : WuBingTai
import os

import uiautomator2 as u2
from pyppeteer import connect

from chromedriver import ChromeDriver
from common.common_config import *
from loguru import logger


def get_driver(device_name):
    """
    初始化driver
    is_clear:清除数据
    :return:
    """
    try:
        d = u2.connect(device_name)
        # d = u2.connect("192.168.129.93")
        # logger.info("设备信息:{}".format(d.info))
        # 设置全局寻找元素超时时间
        d.implicitly_wait(WAIT_TIMEOUT)  # default 20.0
        # 设置点击元素延迟时间
        d.settings['operation_delay'] = CLICK_POST_DELAY
        # d.service("uiautomator").stop()
        # 停止uiautomator 可能和atx agent冲突
        return d
    except Exception as e:
        logger.error(f"初始化driver异常!{e}")


def get_web_driver(d, driver_ip):
    """
    获取设备当前web driver
    :return:wd
    """
    try:
        wd = ChromeDriver(d).driver(driver_ip=driver_ip)
        return wd
    except Exception as e:
        logger.error(f"初始化webdriver异常!{e}")


# pyppeteer，browser和page获取
async def get_browser(devices, port=9516):
    info = os.popen(f"adb  -s {devices} shell grep -a webview_devtools_remote /proc/net/unix").readline()
    logger.debug(info)
    remote = info[info.rfind('remote_') + 7:]
    logger.debug(remote)
    os.popen(f"adb -s {devices} forward tcp:{port} localabstract:webview_devtools_remote_{remote}").readline()
    # ws = requests.get(f"http://localhost:{port}/json/version").json()['webSocketDebuggerUrl']
    ws = f"ws://localhost:{port}/devtools/browser"
    logger.debug(ws)
    browser = await connect(
        {
            'browserWSEndpoint': ws,
            'defaultViewport': None
        }
    )
    return browser


async def get_page(browser, flag="default"):
    pages = await browser.pages()
    flag_page = pages[0]
    if flag != "default":
        for page in pages:
            if flag in await page.title():
                flag_page = page
                break
    return flag_page
