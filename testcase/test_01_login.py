# -*- coding: utf-8 -*-
# @Time    : 2023/2/15 15:14
# @Author  : WuBingTai
import time

import pytest
import allure

from pages.login import Login
from test_user_config import *
from loguru import logger


@pytest.mark.usefixtures('driver_setup')
@pytest.mark.run(order=1)
class TestLogin:

    @pytest.fixture()
    def init(self):
        self.login = Login(self.driver)
        logger.info("初始化登录模块")
        yield self.login
        logger.info("结束登录模块")

    @allure.story('测试登录')
    @pytest.mark.P0
    def test_login(self, init):
        if self.login.is_in_login():
            init.login(user[0])
            time.sleep(3)
        self.login.assert_login()
