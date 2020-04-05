#!/bin/bash

cd /root/kangaroo_scrapy/
PATH=$PATH:/usr/local/bin
export PATH
scrapy crawl toscrape-xpath
