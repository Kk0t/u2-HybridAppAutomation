# u2-HybridAppAutomation

此项目适用于Hybrid app,原生部分使用uiautomator2；

webview探索了2种实现方案

1、Chromedriver方式，经典方案，缺点是运行速度慢，需要匹配Chromedriver版本

2、基于CDP协议的pyppeteer，当然你也可以选择其他如playwright的框架来实现

使用环境

Python 3.7+

uiautomator2  2.16.22

pyppeteer  1.0.2

Chromedriver环境

selenium 3.141.0（这个版本稳定，配合项目中版本的chromedriver使用，大部分安卓机型可正常使用）

Chromedriver.exe 71.0.3578

这个配置亲测适用于webview 70 80 90 100 110等几个版本，运行稳定

建议使用CDP协议方式来操作webview，一起愉快玩转webview
