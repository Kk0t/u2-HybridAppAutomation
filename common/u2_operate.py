# -*- coding: utf-8 -*-
# @Time    : 2023/2/7 15:00
# @Author  : WuBingTai
import re

from loguru import logger


class Base(object):
    def __init__(self, driver):
        self.d = driver
        self.width = self.get_window_size()[0]
        self.height = self.get_window_size()[1]

    def by(self, element):
        """
        :param element:
        :return:
        """
        if str(element).startswith("com"):
            return self.d(resourceId=element)
        elif re.findall("//", str(element)):
            return self.d.xpath(element)
        else:
            return self.d(description=element)

    def click(self, element):
        """
        :param element:
        :return:
        """
        self.by(element).click(timeout=10)

    def send_text(self, element, text):
        """
        :param element: 元素
        :param text: 输入文本
        :return:
        """
        self.by(element).set_text(text)

    def get_window_size(self):
        """
        获取屏幕尺寸
        :return:
        """
        window_size = self.d.window_size()
        width = int(window_size[0])
        height = int(window_size[1])
        return width, height

    def app_start(self, package_name):
        """
        打开对应报名app
        :param package_name:
        :return:
        """
        self.d.app_start(package_name)

    def check_elements(self, element, timeout=5):
        """
        检查元素是否存在
        :return:
        """
        is_exited = False
        try:
            while timeout > 0:
                xml = self.d.dump_hierarchy()
                if re.findall(element, xml):
                    is_exited = True
                    print(f"查询到{element}")
                    break
                else:
                    timeout -= 1
        except Exception as e:
            print(f"{element}查找失败!{e}")
        finally:
            return is_exited

    def swipe_find_element(self, element, direction, max_num=10):
        """
        :param element: 元素
        :param direction: 方向
        :param max_num: 最大滑动次数
        :return:
        """
        n = 0
        while not self.by(element).exists:
            self.d.swipe_ext(direction, scale=0.5)
            n += 1
            if n > max_num:
                break
        return self.by(element)

    def element_exists(self, element):
        return self.by(element).exists

    def assert_element(self, element):
        assert self.element_exists(element) is True, f"断言{element}元素存在,失败!"
        logger.info(f"断言{element}元素存在,成功!")
