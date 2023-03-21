# -*- coding: utf-8 -*-
# @Time    : 2023/2/9 18:19
# @Author  : WuBingTai
from loguru import logger

from common.u2_operate import Base

tips = '温馨提示'
agree = '同意'
disagree = '不同意'
phone = '//*/android.view.View/android.widget.EditText[1]'
code = '//*/android.view.View/android.widget.EditText[2]'
agree_icon = '//*/android.view.View/android.widget.ImageView[1]'
login_but = '//*[@content-desc="登录"]'
main_room = '//*/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ImageView[1]'


class Login(Base):

    def __init__(self, driver):
        self.d = driver
        self.base = Base(self.d)

    def check_tips(self):
        return self.check_elements(tips)

    def click_agree(self):
        self.click(agree)

    def click_disagree(self):
        self.click(disagree)

    def send_phone(self, text):
        self.send_text(phone, text)

    def send_code(self, text):
        self.send_text(code, text)

    def select_agree_icon(self):
        self.click(agree_icon)

    def click_login_but(self):
        self.click(login_but)

    def is_in_login(self):
        return self.element_exists(login_but)

    def login(self, user):
        try:
            if self.check_tips():
                self.click_agree()
            self.send_phone(user.get('phone'))
            self.send_code(user.get('code'))
            self.select_agree_icon()
            self.click_login_but()
        except Exception as e:
            logger.error(f"login异常!{e}")

    def assert_login(self):
        self.assert_element(main_room)
