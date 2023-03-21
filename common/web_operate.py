# -*- coding: utf-8 -*-
# @Time    : 2023/2/3 11:23
# @Author  : WuBingTai
import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common.common_config import *


class WebOperate(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        element = WebDriverWait(self.driver, TIMEOUT).until(
            EC.visibility_of_element_located(locator))
        return element

    def find_elements(self, locator: object) -> object:
        elements = WebDriverWait(self.driver, TIMEOUT).until(
            EC.visibility_of_any_elements_located(locator))
        return elements

    def click(self, locator):
        """
        点击操作
        Usage:
        locator = ("id","xxx")
        driver.click(locator)
        """
        element = self.find_element(locator)
        element.click()

    def clicks(self, locator, index):
        """
        点击操作
        Usage:
        locator = ("id","xxx")
        driver.click(locator)
        """
        elements = self.find_elements(locator)
        # elements[index].location_once_scrolled_into_view
        elements[index].click()

    def send_key(self, locator, text):
        """
        发送文本，清空后输入
        Usage:
        locator = ("id","xxx")
        driver.send_keys(locator, text)
        """
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def send_keys(self, locator, index, text):
        """
        发送文本，清空后输入，适用于elements
        """
        elements = self.find_elements(locator)
        elements[index].clear()
        elements[index].send_keys(text)

    def is_text_in_element(self, locator, text, timeout=10):
        """
        判断文本在元素里,没定位到元素返回False，定位到返回判断结果布尔值
        result = driver.text_in_element(locator, text)
        """
        try:
            result = WebDriverWait(self.driver, timeout, 1).until(
                EC.text_to_be_present_in_element(locator, text))
        except TimeoutException:
            print("元素没定位到：" + str(locator))
            return False
        else:
            return result

    def is_text_in_value(self, locator, value, timeout=10):
        """
        判断元素的value值，没定位到元素返回false,定位到返回判断结果布尔值
        result = driver.text_in_element(locator, text)
        """
        try:
            result = WebDriverWait(self.driver, timeout, 1).until(
                EC.text_to_be_present_in_element_value(locator, value))
        except TimeoutException:
            print("元素没定位到：" + str(locator))
            return False
        else:
            return result

    def is_title(self, title, timeout=10):
        """判断title完全等于"""
        result = WebDriverWait(self.driver, timeout, 1).until(EC.title_is(title))
        return result

    def is_title_contains(self, title, timeout=10):
        """判断title包含"""
        result = WebDriverWait(self.driver, timeout, 1).until(EC.title_contains(title))
        return result

    def is_selected(self, locator, timeout=10):
        """判断元素被选中，返回布尔值,"""
        result = WebDriverWait(self.driver, timeout, 1).until(EC.element_located_to_be_selected(locator))
        return result

    def is_selected_be(self, locator, selected=True, timeout=10):
        """判断元素的状态，selected是期望的参数true/False
        返回布尔值"""
        result = WebDriverWait(self.driver, timeout, 1).until(
            EC.element_located_selection_state_to_be(locator, selected))
        return result

    def is_alert_present(self, timeout=10):
        """判断页面是否有alert，有返回alert(注意这里是返回alert,不是True)
        没有返回False"""
        result = WebDriverWait(self.driver, timeout, 3).until(EC.alert_is_present())
        return result

    def is_visibility(self, locator: object) -> object:
        """元素可见返回本身，不可见返回Fasle"""
        '元素可见返u回Tre，不可见返回Fasle'
        try:
            WebDriverWait(self.driver, TIMEOUT).until(
                EC.visibility_of_any_elements_located(locator))
            return True
        except TimeoutException:
            return False

    def is_invisibility(self, locator, timeout=10):
        """元素可见返回本身，不可见返回True，没找到元素也返回True"""
        '''元素不可见返回True，可见返回Fasle'''
        try:
            WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def is_clickable(self, locator, timeout=10):
        """元素可以点击is_enabled返回本身，不可点击返回Fasle"""
        result = WebDriverWait(self.driver, timeout, 1).until(EC.element_to_be_clickable(locator))
        return result

    def is_located(self, locator, timeout=10):
        """判断元素有没被定位到（并不意味着可见），定位到返回element,没定位到返回False"""
        result = WebDriverWait(self.driver, timeout, 1).until(EC.presence_of_element_located(locator))
        return result

    def move_to_element(self, locator):
        """
        鼠标悬停操作
        Usage:
        locator = ("id","xxx")
        driver.move_to_element(locator)
        """
        element = self.find_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def back(self):
        """
        Back to old window.
        Usage:
        driver.back()
        """
        self.driver.back()

    def forward(self):
        """
        Forward to old window.
        Usage:
        driver.forward()
        """
        self.driver.forward()

    def close(self):
        """
        Close the windows.
        Usage:
        driver.close()
        """
        self.driver.close()

    def quit(self):
        """
        Quit the driver and close all the windows.
        Usage:
        driver.quit()
        """
        self.driver.quit()

    def get_title(self):
        """获取title"""
        return self.driver.title

    def get_text(self, locator):
        """获取文本"""
        element = self.find_element(locator)
        return element.text

    def get_texts(self, locator, index):
        """获取文本"""
        elements = self.find_elements(locator)
        return elements[index].text

    def get_attribute(self, locator, name):
        """获取属性"""
        element = self.find_element(locator)
        return element.get_attribute(name)

    def js_execute(self, js):
        """执行js"""
        time.sleep(0.5)
        return self.driver.execute_script(js)

    def js_click(self, locator):
        el = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", el)

    def js_clicks(self, locator, index):
        els = self.find_elements(locator)
        self.driver.execute_script(f"arguments[0].click();", els[index])

    def js_focus_element(self, locator):
        """聚焦元素"""
        target = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def js_scroll_top(self):
        """滚动到顶部"""
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)

    def js_scroll_end(self):
        """滚动到底部"""
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)

    def js_get_elements_length(self, locator):
        """
        driver未提供此方法，故用js补充
        :param locator:
        :return: 返回元素长度
        """
        time.sleep(0.5)
        js = f"return  document.querySelectorAll('{locator[1]}').length"
        return self.driver.execute_script(js)

    def getSize(self):
        """获得机器屏幕大小x,y
        :return: x, y
        """
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    @staticmethod
    def switch_window(driver, index=-1):
        """
        切换webview窗口，多窗口时使用，idnex = -1为最新的页面
        :param index:
        :return:
        """
        # 获取最新window_handles数据需等待一会，故暂停5s
        time.sleep(3)
        windows = driver.window_handles
        driver.switch_to.window(windows[index])
