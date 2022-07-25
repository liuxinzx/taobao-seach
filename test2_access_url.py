'''
通过搜索获取商品信息
'''

from utils import create_chrome_driver, add_cookies

browser = create_chrome_driver()  # 创建谷歌浏览器对象，通过控制浏览器来访问url
browser.get('https://www.taobao.com')
add_cookies(browser, 'taobao2.json')
browser.get('https://s.taobao.com/search?q=手机&s=0')  # 淘宝上的搜索功能必须要登录才能搜索，需要用cookie来亮明身份