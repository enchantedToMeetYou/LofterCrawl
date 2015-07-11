# -*- coding: utf-8 -*-

# Scrapy settings for lofter project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'lofter'

SPIDER_MODULES = ['lofter.spiders']
NEWSPIDER_MODULE = 'lofter.spiders'

ITEM_PIPELINES = {'lofter.pipelines.LofterPipeline': 1}

DOWNLOAD_DELAY = 0.25
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'lofter (+http://www.yourdomain.com)'
