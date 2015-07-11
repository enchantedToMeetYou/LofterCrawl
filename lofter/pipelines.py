# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import requests
import os
import sys

FILE_PATH = os.path.split(os.path.realpath(__file__))[0]
sys.path.append('{0}/data_access'.format(FILE_PATH))
from mysql_manager import MysqlManager

class LofterPipeline(object):
    def process_item(self, item, spider):
        if 'image_urls' in item:
           dir_path = '{0}/../../LofterImageSets'.format(FILE_PATH)
           if not os.path.exists(dir_path):
               os.makedirs(dir_path)
           for image_url in item['image_urls']:
               image_name = image_url.split('/')[-1]
               file_path = '%s/%s' % (dir_path, image_name)
               if os.path.exists(file_path):
                   continue

               #database operation
               category_list = item['image_category']
               category=[] 
               for cat in category_list:
                   category.append(cat.strip('#'))
               category_tag = ','.join(category)

               image_set_name = item['query_url'][0].split('/')[-1]
               description = item['description'][0].encode('utf-8')
               field_item = [(image_set_name,image_name,category_tag,description,image_url,item['query_url'][0])*2]
               MysqlManager.insert_items_into_photos(field_item)            
               with open(file_path, 'wb') as handle:
                   response = requests.get(image_url, stream=True)
                   for block in response.iter_content(1024):
                       if not block:
                           break
                       handle.write(block)

        return item
