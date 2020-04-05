# -*- coding: utf-8 -*-
import scrapy, json, datetime, csv, requests, re
from quotesbot.items import QuotesbotItem
from scrapy.http.request import Request

class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'toscrape-xpath'
    # start_urls = [
    #     'http://quotes.toscrape.com/',
    # ]
    product_str = """https://h5api.m.taobao.com/h5/mtop.taobao.detail.getdetail/6.0/?jsv=2.5.1&appKey=12574478&t=1574859197936&sign=396333ba06f8637b2bb97c6631274341&api=mtop.taobao.detail.getdetail&v=6.0&isSec=0&ecode=0&AntiFlood=true&AntiCreep=true&H5Request=true&ttid=2018%40taobao_h5_9.9.9&type=jsonp&dataType=jsonp&callback=&data=%7B%22id%22%3A%22{item_id}%22%2C%22itemNumId%22%3A%22{item_id}%22%2C%22itemId%22%3A%22{item_id}%22%2C%22exParams%22%3A%22%7B%5C%22id%5C%22%3A%5C%22{item_id}%5C%22%7D%22%2C%22detail_v%22%3A%228.0.0%22%2C%22utdid%22%3A%221%22%7D"""

    tagRuleList = [
{"shopName":"爱玩电玩数码精品店","shopId":"165780471","tagRule":'''{"withCover": {"rule": {"is": ["\\u6807\\u51c6\\u7248\\uff08\\u76d2\\u88c5\\uff09", "\\u6807\\u51c6\\u7248"]}, "name": "\\u5e26\\u58f3"}, "withoutCover": {"rule": {"is": ["\\u5176\\u4ed6"]}, "name": "\\u4e0d\\u5e26\\u58f3"}}'''},    
{"shopName":"藏宝海湾 GAME","shopId":"58920150","tagRule":'''{"withCover": {"rule": {"is": ["\\u6807\\u51c6\\u7248"]}, "name": "\\u5e26\\u58f3"}, "withoutCover": {"rule": {"is": ["\\u7b80\\u88c5\\u7248"]}, "name": "\\u4e0d\\u5e26\\u58f3"}}'''},  
{"shopName":"畅玩幸运星电玩","shopId":"63727730","tagRule":'''{"withCover": {"rule": {"is": ["\\u6807\\u51c6\\u7248\\uff08\\u76d2\\u88c5\\uff09", "\\u6807\\u51c6\\u7248"]}, "name": "\\u5e26\\u58f3"}, "withoutCover": {"rule": {"is": ["\\u7b80\\u88c5\\u7248"]}, "name": "\\u4e0d\\u5e26\\u58f3"}}'''},    
{"shopName":"辰租电玩","shopId":"305462602","tagRule":'''{"withCover": {"rule": {"is": ["\\u6807\\u51c6\\u7248\\uff08\\u76d2\\u88c5\\uff09", "\\u6807\\u51c6\\u7248"]}, "name": "\\u5e26\\u58f3"}, "withoutCover": {"rule": {"is": ["\\u7b80\\u88c5\\u7248"]}, "name": "\\u4e0d\\u5e26\\u58f3"}}'''},    
{"shopName":"好玩专业电玩店","shopId":"57185484","tagRule":'''{"withCover": {"rule": {"is": ["\\u7b80\\u88c5\\u7248"]}, "name": "\\u5e26\\u58f3"}}'''},  
{"shopName":"红蓝白游戏王国","shopId":"137667186","tagRule":'''{"withCover": {"rule": {"is": ["\\u6807\\u51c6\\u7248\\uff08\\u76d2\\u88c5\\uff09", "\\u6807\\u51c6\\u7248"]}, "name": "\\u5e26\\u58f3"}, "withoutCover": {"rule": {"is": ["\\u7b80\\u88c5\\u7248"]}, "name": "\\u4e0d\\u5e26\\u58f3"}}'''},    
{"shopName":"葫芦娃电玩","shopId":"113086697","tagRule":'''{"withCover": {"rule": {"is": ["\\u6807\\u51c6\\u7248\\uff08\\u76d2\\u88c5\\uff09", "\\u6807\\u51c6\\u7248"]}, "name": "\\u5e26\\u58f3"}, "withoutCover": {"rule": {"is": ["\\u7b80\\u88c5\\u7248"]}, "name": "\\u4e0d\\u5e26\\u58f3"}}'''},    
{"shopName":"决战电玩 专业电玩","shopId":"35626532","tagRule":'''{"withCover": {"rule": {"is": ["\\u6807\\u51c6\\u7248\\uff08\\u76d2\\u88c5\\uff09", "\\u6807\\u51c6\\u7248"]}, "name": "\\u5e26\\u58f3"}, "withoutCover": {"rule": {"is": ["\\u7b80\\u88c5\\u7248"]}, "name": "\\u4e0d\\u5e26\\u58f3"}}'''},    
{"shopName":"蓝精灵电玩","shopId":"324309940","tagRule":'''{"withCover": {"rule": {"is": ["\\u6807\\u51c6\\u7248\\uff08\\u76d2\\u88c5\\uff09", "\\u6807\\u51c6\\u7248"]}, "name": "\\u5e26\\u58f3"}, "withoutCover": {"rule": {"is": ["\\u7b80\\u88c5\\u7248"]}, "name": "\\u4e0d\\u5e26\\u58f3"}}'''},    
{"shopName":"老米电玩","shopId":"103684887","tagRule":'''{"withCover": {"rule": {"is": ["\\u6807\\u51c6\\u7248\\uff08\\u76d2\\u88c5\\uff09", "\\u6807\\u51c6\\u7248"]}, "name": "\\u5e26\\u58f3"}, "withoutCover": {"rule": {"is": ["\\u7b80\\u88c5\\u7248"]}, "name": "\\u4e0d\\u5e26\\u58f3"}}'''},    
{"shopName":"龙之购电玩","shopId":"116874181","tagRule":'''{"withCover": {"rule": {"is": ["\\u6807\\u51c6\\u7248\\uff08\\u76d2\\u88c5\\uff09", "\\u6807\\u51c6\\u7248"]}, "name": "\\u5e26\\u58f3"}, "withoutCover": {"rule": {"is": ["\\u7b80\\u88c5\\u7248"]}, "name": "\\u4e0d\\u5e26\\u58f3"}}'''},    
{"shopName":"萌牛电玩游戏世界","shopId":"65538372","tagRule":'''{"withCover": {"rule": {"is": ["\\u6807\\u51c6\\u7248\\uff08\\u76d2\\u88c5\\uff09", "\\u6807\\u51c6\\u7248"]}, "name": "\\u5e26\\u58f3"}, "withoutCover": {"rule": {"is": ["\\u7b80\\u88c5\\u7248"]}, "name": "\\u4e0d\\u5e26\\u58f3"}}'''},    
{"shopName":"南昌圆梦玩家","shopId":"62705357","tagRule":'''{"withCover": {"rule": {"is": ["\\u6807\\u51c6\\u7248"]}, "name": "\\u5e26\\u58f3"}, "withoutCover": {"rule": {"is": ["\\u7b80\\u88c5\\u7248"]}, "name": "\\u4e0d\\u5e26\\u58f3"}}'''},    
{"shopName":"鸟木星云电玩","shopId":"107266586","tagRule":'''{"withCover": {"rule": {"is": ["\\u6807\\u51c6\\u7248\\uff08\\u76d2\\u88c5\\uff09"]}, "name": "\\u5e26\\u58f3"}, "withoutCover": {"rule": {"is": ["\\u7b80\\u88c5\\u7248"]}, "name": "\\u4e0d\\u5e26\\u58f3"}}'''},   
{"shopName":"宁波哒哒电玩","shopId":"35713044","tagRule":'''{"withCover": {"rule": {"is": ["\\u6807\\u51c6\\u7248\\uff08\\u76d2\\u88c5\\uff09"]}, "name": "\\u5e26\\u58f3"}, "withoutCover": {"rule": {"is": ["\\u7b80\\u88c5\\u7248"]}, "name": "\\u4e0d\\u5e26\\u58f3"}}'''},    
{"shopName":"宁波老猎人电玩","shopId":"255640440","tagRule":'''{"withCover": {"rule": {"all": None}, "name": "\\u5e26\\u58f3"}}'''},  
{"shopId":"255640440","shopName":"宁波老猎人电玩", "tagRule":'''{"withCover": {"rule": {"all": null}, "name": "\\u5e26\\u58f3"}}'''},
{"shopName":"泡儿电玩","shopId":"63159848","tagRule":'''{"withCover": {"rule": {"is": ["\\u6807\\u51c6\\u7248\\uff08\\u76d2\\u88c5\\uff09"]}, "name": "\\u5e26\\u58f3"}, "withoutCover": {"rule": {"is": ["\\u7b80\\u88c5\\u7248"]}, "name": "\\u4e0d\\u5e26\\u58f3"}}'''},   
{"shopName":"上海潮玩电玩","shopId":"60924356","tagRule":'''{"withCover": {"rule": {"is": ["\\u6807\\u51c6\\u7248\\uff08\\u76d2\\u88c5\\uff09"]}, "name": "\\u5e26\\u58f3"}, "withoutCover": {"rule": {"is": ["\\u7b80\\u88c5\\u7248"]}, "name": "\\u4e0d\\u5e26\\u58f3"}}'''},  
{"shopName":"神秘时空电玩","shopId":"109840779","tagRule":'''{"withCover": {"rule": {"is": ["\\u6807\\u51c6\\u7248\\uff08\\u76d2\\u88c5\\uff09", "\\u6807\\u51c6\\u7248"]}, "name": "\\u5e26\\u58f3"}, "withoutCover": {"rule": {"is": ["\\u7b80\\u88c5\\u7248"]}, "name": "\\u4e0d\\u5e26\\u58f3"}}'''},    
{"shopName":"神游电玩 广州店","shopId":"104709370","tagRule":'''{"withCover": {"rule": {"is": ["\\u6807\\u51c6\\u7248\\uff08\\u76d2\\u88c5\\uff09", "\\u6807\\u51c6\\u7248"]}, "name": "\\u5e26\\u58f3"}, "withoutCover": {"rule": {"is": ["\\u7b80\\u88c5\\u7248"]}, "name": "\\u4e0d\\u5e26\\u58f3"}}'''},  
{"shopName":"玩乐多电玩","shopId":"148873281","tagRule":'''{"withCover": {"rule": {"is": ["\\u6807\\u51c6\\u7248"]}, "name": "\\u5e26\\u58f3"}, "withoutCover": {"rule": {"is": ["\\u7b80\\u88c5\\u7248"]}, "name": "\\u4e0d\\u5e26\\u58f3"}}'''},   
{"shopName":"屋檐大叔","shopId":"422801835","tagRule":'''{"withCover": {"rule": {"is": ["\\u7b80\\u88c5\\u7248"]}, "name": "\\u5e26\\u58f3"}}'''},   
{"shopName":"信仰电玩租赁店","shopId":"64805224","tagRule":'''{"withCover": {"rule": {"is": ["\\u6807\\u51c6\\u7248"]}, "name": "\\u5e26\\u58f3"}}'''},    
{"shopName":"芸峰海螺电玩","shopId":"105568708","tagRule":'''{"withCover": {"rule": {"is": ["\\u6807\\u51c6\\u7248\\uff08\\u76d2\\u88c5\\uff09", "\\u6807\\u51c6\\u7248"]}, "name": "\\u5e26\\u58f3"}, "withoutCover": {"rule": {"is": ["\\u7b80\\u88c5\\u7248"]}, "name": "\\u4e0d\\u5e26\\u58f3"}}'''},   
{"shopName":"中古游戏世界","shopId":"434614556","tagRule":'''{"withCover": {"rule": {"is": ["\\u6807\\u51c6\\u7248\\uff08\\u76d2\\u88c5\\uff09", "\\u666e\\u901a\\u7248"]}, "name": "\\u5e26\\u58f3"}, "withoutCover": {"rule": {"is": ["\\u7b80\\u88c5\\u7248","\\u5ec9\\u4ef7\\u7248"]}, "name": "\\u4e0d\\u5e26\\u58f3"}}'''},    
{"shopName":"最近电玩","shopId":"404139719","tagRule":'''{"withCover": {"rule": {"is": ["\\u6807\\u51c6\\u7248"]}, "name": "\\u5e26\\u58f3"}, "withoutCover": {"rule": {"is": ["\\u7b80\\u88c5\\u7248"]}, "name": "\\u4e0d\\u5e26\\u58f3"}}'''},   
{"shopName":"FF天幻电玩","shopId":"352561239","tagRule":'''{"withCover": {"rule": {"is": ["\\u6807\\u51c6\\u7248\\uff08\\u76d2\\u88c5\\uff09"]}, "name": "\\u5e26\\u58f3"}, "withoutCover": {"rule": {"is": ["\\u7b80\\u88c5\\u7248"]}, "name": "\\u4e0d\\u5e26\\u58f3"}}'''},   
    ]
# 乐波游戏
# 林克电玩
# 上海澎澎电玩
    items_url = "http://111.231.110.192:8080/product/taobao"
    tagRule_url = "http://111.231.110.192:8080/product/store"
    start_urls = ["http://www.taobao.com"]
    def parse(self, response):
        items = requests.get(self.items_url).json()['data']
        #items = [595482361488]#595444936866] #589320166593,599102513060,608191533062,605583515492,593095297666,600401864239,595664445560,590973381653,609926308012]
        self.tagRule = {}
        tagRules = self.tagRuleList #requests.get(self.tagRule_url).json()['data']
        for tagRule in tagRules:
            self.tagRule[str(tagRule['shopId'])] = tagRule['tagRule']
        # for tagRule in self.tagRuleList:
        #     self.tagRule[tagRule['shopId']] = tagRule['tagRule']
        for item in items:
            item_id = item['itemId']
            yield Request(self.product_str.format(item_id=item_id),meta={'shopId':item['storeId']},callback=self.parse2)

    # def __init__(self):
    #     self.start_urls = []
    #     with open('/Users/wuting/Downloads/taobao_new/item_ids.csv') as f:
    #         items =[line.strip() for line in f.readlines()]
    #         #items = [589320166593,599102513060,608191533062,605583515492,593095297666,600401864239,595664445560,590973381653,609926308012]
    #     for item_id in items:
    #         self.start_urls.append(self.product_str.format(item_id=item_id))
    #     self.tagRule = {}
    #     for tagRule in self.tagRuleList:
    #         self.tagRule[tagRule['shopId']] = tagRule['tagRule']
    #     super(ToScrapeSpiderXPath, self).__init__()

    def parse2(self, response):
        jsonresponse = json.loads(response.body_as_unicode())
        if not jsonresponse['data'].get('item'):
            try:
                itemId = int(re.search(r"itemId%22%3A%(\d+?)%22%2C%22",response.url).groups()[0])
            except:
                print('errrrrror {}'.format(response.url))
                return
            print('item remove https://h5.m.taobao.com/awp/core/detail.htm?id={}'.format(itemId))
            item = QuotesbotItem()
            item['deleted'] = True
            item['shopId'] = response.meta["shopId"]
            item['itemId'] = itemId
            yield item
            return

        itemName = jsonresponse['data']['item']['title']
        itemId = jsonresponse['data']['item']['itemId']
        shopId = jsonresponse['data']['seller']['shopId']
        shopName = jsonresponse['data']['seller']['shopName']
        shopFans = jsonresponse['data']['seller']['fans']
        data = jsonresponse["data"]["apiStack"][0]["value"]
        detail = json.loads(data)
        skuBase = jsonresponse["data"]["skuBase"]
        skuCore = detail["skuCore"]
        sku2info = skuCore["sku2info"]
        #MockData = jsonresponse["data"]["mockData"]

	#If mockData:
        #    json.loads(mockData).get('skuCore', {}).get('sku2info', {})
        
        skus = skuBase['skus']
        print('item get https://h5.m.taobao.com/awp/core/detail.htm?id={}'.format(itemId))
        if self.tagRule.get(str(shopId)):
            tagRule = json.loads(self.tagRule.get(shopId))
        else:
            print("not found shop {}".format(shopId))
            tagRule = None

        for sku in skus:
            skuId = sku["skuId"]
            if sku2info:
                quantity = sku2info.get(skuId,{}).get('quantity', 0)
            else:
                quantity = 0
            desc = {}
            sku_info_pri_quan = sku2info.get(skuId)
            if sku_info_pri_quan:
                skuPrice = sku_info_pri_quan["price"]["priceText"]
            prop = ''
            prop1=sku['propPath'].split(';')
            for j in prop1:
                prop2=j.split(':')
                for pid in skuBase['props']:
                    if pid['pid']==prop2[0]:
                        for vid in pid['values']:
                            if vid['vid']==prop2[1]:
                                prop=prop+vid['name']
                                desc[pid['name']] = vid['name'] 
            # tag
            showTag = None
            if tagRule:
                # {'withCover': {'name': '带壳', 'rule': {'<operator>': <tagWord>}},
                # 'withoutCover': {'name': '不带壳', 'rule': {'<operator>': <tagWord>}}}
                # operator: ['is', 'all', 'in']
                # tagWord:当operator是is时，tagWord是list类型. sku规格描述词只要等于tagWord中某个词就是可以被标记
                # tagWord:当operator是in时，tagWord是in类型
                # tagWord:当operator是all时
                for ruleDetail in tagRule.values():
                    for operator, tagWord in ruleDetail['rule'].items():
                            for descValue in desc.values():
                                if (operator == 'is' and [tg for tg in tagWord if descValue==tg ]) \
                                     or (operator == 'in' and tagWord in descValue) \
                                     or operator == 'all':
                                    showTag = ruleDetail['name']
                                    break

            item = QuotesbotItem()
            item['itemName'] = itemName #任天堂二手Switch游戏 NS 宝可梦 剑盾 口袋妖怪 宠物小精灵 现货, #商品名称
            item['itemId'] = itemId #607365392889, #商品ID
            item['skuId'] = skuId #4435585594534, #skuId
            item['desc'] = desc #"{'软件形式': '标准版', '语种分类': '简体中文'}", #商品规格
            item['price'] = skuPrice #295.00, #商品价格
            item['shopId'] = str(shopId) #"255640440", #shopid
            item['shopName'] = shopName #"宁波老猎人电玩", #店铺名称
            item['showTag'] = showTag #"带游戏壳" #展示标签
            item['itemUrl'] = "https://h5.m.taobao.com/awp/core/detail.htm?id={}".format(item['itemId']) #商品链接
            item['updateTime'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") # "2020-01-01 00:00:00" #爬虫更新时间
            item['deleted'] = False if int(quantity)!=0 else True
            yield item

