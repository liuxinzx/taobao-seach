# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql
from itemadapter import ItemAdapter
import openpyxl
from scrapy.crawler import Crawler


class TaospiderPipeline:

    def __init__(self):
        self.wb = openpyxl.Workbook()  # 创建工作簿
        self.ws = self.wb.active  # 拿到默认激活的工作表
        self.ws.title = 'TaoBaoData'  # 工作表名称
        self.ws.append(('标题','价格','销量','店铺名称','店铺地址' , 'url'))  # 表头

    def close_spider(self, spider):  # 爬虫停止运行的时候执行该方法,钩子函数，自己执行不需要调用
        self.wb.save('淘宝商品数据.xlsx')


    def process_item(self, item, spider):
        title = item.get('title', '')  # 如果字典中的title值为空的话，就把''（空值）赋给title变量,写法一
        price = item.get('price') or 0  # 如果字典中的title值为空的话，就把''（空值）赋给title变量，写法二
        deal_count = item.get('deal_count', '')
        shop = item.get('shop', '')
        location = item.get('location', '')
        url = item.get('url','')
        self.ws.append((title, price, deal_count, shop, location,url))  #
        return item

# class DbPipeline:
#
#     @classmethod
#     def from_crawler(cls, crawler: Crawler):
#         host = crawler.settings['DB_HOST']
#         port = crawler.settings['DB_PORT']
#         username = crawler.settings['DB_USER']
#         password = crawler.settings['DB_PASS']
#         database = crawler.settings['DB_NAME']
#         return cls(host, port, username, password, database)  # 类的构造器
#
#     def __init__(self, host, port, username, password, database):
#         self.conn = pymysql.connect(host=host, port=port,
#                                     user=username, password=password,
#                                     database=database, charset='utf8',
#                                     autocommit=True)
#         self.cursor = self.conn.cursor()
#         self.data = []  # 负责存储每次爬取返回的数据
#
#     def close_spider(self, spider):
#         if len(self.data) > 0:  # 如果剩下的数据没超过100条，在这里判断写入数据库
#             self._write_to_db()
#         self.conn.close()
#
#     def process_item(self, item, spider):
#         title = item.get('title', '')  # 如果字典中的title值为空的话，就把''（空值）赋给title变量,写法一
#         rating_num = item.get('rating_num') or 0  # 如果字典中的title值为空的话，就把''（空值）赋给title变量，写法二
#         inq = item.get('inq', '')
#         duration = item.get('duration', '')
#         intro = item.get('intro', '')
#         self.data.append((title, rating_num, inq, duration, intro))  # 先把数据存入容器
#         if len(self.data) == 100:  # 每100条数据写入一次
#             self._write_to_db()
#             self.data.clear()
#         return item  # 如果这里不return,那么后面的管道就拿不到数据了
#
#     def _write_to_db(self):
#         self.cursor.executemany(
#             'insert into douban (title, rating_num, inq, duration, intro) values (%s, %s, %s, %s, %s, %s )',
#             self.data
#         )
#         self.conn.commit()

