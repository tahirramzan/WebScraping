# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WebscrapingItem(scrapy.Item):
    # define the fields for your item here like:
    Product_ID = scrapy.Field()
    Product_Category = scrapy.Field()
    Product_Sub_category = scrapy.Field()
    Product_Name = scrapy.Field()
    Product_Price = scrapy.Field()
    Product_Description = scrapy.Field()
    Product_Rating = scrapy.Field()
    Product_Image = scrapy.Field()
    Product_URL = scrapy.Field()
    Number_Of_Ratings = scrapy.Field()
    Reviews = scrapy.Field()
