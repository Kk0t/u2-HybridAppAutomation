# -*- coding: utf-8 -*-
# @Time    : 2023/2/17 16:02
# @Author  : WuBingTai
from loguru import logger
from selenium.webdriver.common.by import By

from common.pyppeteer_operate import PageBase
from common.web_operate import WebOperate

room_name = (By.CSS_SELECTOR, 'input.createroom-input')
room_desc = (By.CSS_SELECTOR, 'textarea.createroom-input.createroom-textarea')
set_key_btn = (By.CSS_SELECTOR, 'button.zk-switch')
scene = (By.CSS_SELECTOR, 'li.sceneselector-cr-scene')
create_btn = (By.CSS_SELECTOR, 'button.zk-button')
dialog_title = (By.CSS_SELECTOR, 'p.sucnotice-rd-title')
dialog_confirm = (By.CSS_SELECTOR, 'button.zk-dialog-btn-confirm')
dialog_btn = (By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/button[1]')
failnotice_title = (By.CSS_SELECTOR, 'h3.failnotice-rd-title')


#
# class CreateRoom(WebOperate):
#     def __init__(self, driver):
#         self.driver = driver
#         WebOperate.switch_window(self.driver)
#         self.wd = WebOperate(self.driver)
#
#     def send_room_name(self, name):
#         self.send_key(room_name, name)
#
#     def send_room_desc(self, desc):
#         self.send_key(room_desc, desc)
#
#     def click_set_key_btn(self):
#         self.click(set_key_btn)
#
#     def click_scene(self, index):
#         self.clicks(scene, index)
#
#     def click_create_btn(self):
#         self.click(create_btn)
#
#     def get_dialog_title(self):
#         return self.get_text(dialog_title)
#
#     def click_dialog_confirm(self):
#         self.click(dialog_confirm)
#
#     def click_dialog_btn(self):
#         self.click(dialog_btn)
#
#     def get_failnotice_title(self):
#         return self.get_text(failnotice_title)
#
#     def create_room(self, name, desc, scene_index=0, set_key=True):
#         try:
#             self.send_room_name(name)
#             self.send_room_desc(desc)
#             if set_key:
#                 self.click_set_key_btn()
#             self.click_scene(scene_index)
#             self.click_create_btn()
#         except Exception as e:
#             logger.error(f"create_roomy异常!{e}")
#

class CreateRoom(WebOperate):
    def __init__(self, page):
        self.page = PageBase(page)

    def send_room_name(self, name):
        self.page.send_key(room_name[1], name)

    def send_room_desc(self, desc):
        self.page.send_key(room_desc[1], desc)

    def click_set_key_btn(self):
        self.page.click(set_key_btn[1])

    def click_scene(self, index):
        self.page.clicks(scene[1], index)

    def click_create_btn(self):
        self.page.click(create_btn[1])

    def get_dialog_title(self):
        return self.page.get_text(dialog_title[1])

    def click_dialog_confirm(self):
        self.page.click(dialog_confirm[1])

    def click_dialog_btn(self):
        self.page.click(dialog_btn[1])

    def get_failnotice_title(self):
        return self.page.get_text(failnotice_title[1])

    def create_room(self, name, desc, scene_index=0, set_key=True):
        try:
            self.send_room_name(name)
            self.send_room_desc(desc)
            if set_key:
                self.click_set_key_btn()
            self.click_scene(scene_index)
            self.click_create_btn()
        except Exception as e:
            logger.error(f"create_roomy异常!{e}")
