# -*- coding: utf-8 -*-
# @Time    : 2023/3/10 16:27
# @Author  : WuBingTai
import asyncio


class BrowserBase(object):
    def __init__(self, browser):
        self.loop = asyncio.get_event_loop()
        self.browser = browser

    def get_page(self, index):
        page = self.loop.run_until_complete(self.browser.pages())[index]
        return page


# 基础操作封装，把异步封装简化
class PageBase(object):
    def __init__(self, page):
        self.loop = asyncio.get_event_loop()
        self.page = page

    async def find_element(self, element):
        return await self.page.J(element)

    async def find_elements(self, elements):
        return await self.page.JJ(elements)

    def wait_for_selector(self, element):
        self.loop.run_until_complete(self.page.waitForSelector(element))

    def wait_for_time(self, time=500):
        self.loop.run_until_complete(self.page.waitFor(time))

    def click(self, element):
        self.loop.run_until_complete(self.page.click(element))

    def clicks(self, elements, index):
        els = self.loop.run_until_complete(self.find_elements(elements))
        self.loop.run_until_complete(els[index].click())

    def send_key(self, element, text):
        self.loop.run_until_complete(self.page.type(element, text))

    def get_text(self, element):
        return self.loop.run_until_complete(self.page.Jeval(element, "el => el.textContent"))
