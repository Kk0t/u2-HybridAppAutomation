# -*- coding: utf-8 -*-
# @Time    : 2023/2/28 15:13
# @Author  : WuBingTai
import asyncio

import allure
import pytest
from loguru import logger

from driver import get_page, get_browser
from pages.web_create_room import CreateRoom
from pages.meta_home import Home


@pytest.mark.usefixtures('driver_setup')
@pytest.mark.run(order=1)
class TestCreateRoom:



    #chromedirver方式
    # @pytest.fixture()
    # def init(self):
    #     self.home = Home(self.driver)
    #     self.home.click_create_space()
    #     self.create_room = CreateRoom(self.web_driver)
    #     logger.info("初始化创建空间模块")
    #     yield self.create_room
    #     logger.info("结束创建空间模块")
    #
    # @allure.story('测试创建空间')
    # @pytest.mark.P1
    # def test_create_room(self, init):
    #     init.create_room(name='自动化测试空间名', desc='自动化测试简介')
    #     assert init.get_failnotice_title() == '创建失败'


    # pyppeteer等CDP框架方式
    @pytest.fixture()
    def init(self):
        self.home = Home(self.driver)
        self.home.click_create_space()
        self.browser = asyncio.get_event_loop().run_until_complete(get_browser(self.ip))
        self.page = asyncio.get_event_loop().run_until_complete(get_page(self.browser, flag='创建空间'))
        self.create_room = CreateRoom(self.page)
        logger.info("初始化创建空间模块")
        yield self.create_room
        logger.info("结束创建空间模块")

    @allure.story('测试创建空间')
    @pytest.mark.P1
    def test_create_room(self, init):
        init.create_room(name='自动化测试空间名', desc='自动化测试简介')
        assert init.get_failnotice_title() == '创建失败'
