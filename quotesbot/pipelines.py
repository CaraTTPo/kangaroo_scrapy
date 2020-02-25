# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv,json,requests

class QuotesbotPipeline(object):
    sku_url = "http://111.231.110.192:8080/product/price"
    headers = {'Content-Type': 'application/json'}
    def process_item(self, item, spider):
        print(item)
        print("!"*30)
        res = requests.post(self.sku_url, data=json.dumps(dict(item)), headers=self.headers)
        print(res)
        # with open('/Users/wuting/Downloads/taobao_new/taobao_detail.csv', 'a') as csvfile:
        #     spamwriter = csv.writer(csvfile)
        #     spamwriter.writerow( [item['itemName'], item['itemId'], item['skuId'], item['desc'], item['price'], item['shopId'], item['shopName'], item['showTag'], item['itemUrl'], item['updateTime']])
        return item
