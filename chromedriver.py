# -*- coding: utf-8 -*-
# @Time    : 2023/2/1 14:30
# @Author  : WuBingTai

from __future__ import absolute_import

import atexit
import os

import requests
from selenium import webdriver
import subprocess
from loguru import logger


def get_web_version(devices):
    """
    :param devices: 设备ip
    :return: version 前3位大版本
    """
    v = os.popen(
        f"adb -s {devices} shell dumpsys package com.google.android.webview | findstr versionNam").readline()
    l = v[v.find('=') + 1:].split(".")
    return ".".join([str(i) for i in l[0:3]])


def invoke_at(func):
    def parameterized():
        def wrapper(*args, **kwargs):
            # path = "../chromedriver/" + get_web_version(kwargs.get('driver_ip'))
            path = "../chromedriver/71.0.3578"
            logger.debug(path)
            cwd = os.getcwd()
            os.chdir(path)
            try:
                ret = func(*args, **kwargs)
            finally:
                os.chdir(cwd)
            return ret

        return wrapper

    return parameterized()


class ChromeDriver(object):
    def __init__(self, d, port=9515):
        self._d = d
        self._port = port

    def _launch_webdriver(self):
        """
        ChromeDriver from https://registry.npmmirror.com/binary.html?path=chromedriver/
        :return:
        """
        logger.info("start chromedriver instance")
        p = subprocess.Popen(['chromedriver', '--port=' + str(self._port)])
        try:
            p.wait(timeout=2.0)
            return False
        except subprocess.TimeoutExpired:
            return True

    def driver(self, driver_ip=None, package=None, attach=True, activity=None, process=None):
        """
        Args:
            - package(string): default current running app
            - attach(bool): default true, Attach to an already-running app instead of launching the app with a clear data directory
            - activity(string): Name of the Activity hosting the WebView.
            - process(string): Process name of the Activity hosting the WebView (as given by ps).
                If not given, the process name is assumed to be the same as androidPackage.

        Returns:
            selenium driver
        """
        app = self._d.app_current()
        capabilities = {
            'chromeOptions': {
                'androidDeviceSerial': driver_ip or self._d.serial,
                'androidPackage': package or app['package'],
                'androidUseRunningApp': attach,
                'androidProcess': process or app['package'],
                'androidActivity': activity or app['activity'],
            }
        }

        self._launch_webdriver()
        dr = webdriver.Remote('http://localhost:%d' % self._port, capabilities)
        # always quit driver when done
        atexit.register(dr.quit)
        return dr


if __name__ == '__main__':
    # v = get_web_version('192.168.180.187:7890')
    # l = v.split(".")
    # print(".".join([str(i) for i in l[0:3]]))
    print(get_web_version('192.168.180.174:7891'))
