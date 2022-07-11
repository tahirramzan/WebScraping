import scrapy
from ..items import WebscrapingItem

class AmazonMakeupSpider(scrapy.Spider):
    name = 'AmazonMakeup'
    start_urls = [
        'https://www.amazon.com/s?i=specialty-aps&bbn=16225006011&rh=n%3A%2116225006011%2Cn%3A11058281&ref=nav_em__nav_desktop_sa_intl_makeup_0_2_11_2'
    ]

    def parse(self, response):
        all_products = response.css('div.s-main-slot')
        items = WebscrapingItem()

        for products in all_products:
            product_name = products.css('h2.a-size-mini span.a-size-base-plus::text').extract()
            product_price = products.css('span.a-offscreen::text').extract()
            product_rating = products.css('span.a-icon-alt::text').extract()
            product_image = products.css('div.a-section img.s-image::attr(src)').extract()
            product_url = products.css('a.a-link-normal::attr(href)').extract()
            number_of_ratings = products.css('span.a-size-base::text').extract()

            #items['Product_Category'] = 'Skincare'
            items['Product_Category'] = 'Make-Up'
            items['Product_Name'] = product_name
            items['Product_Price'] = product_price
            items['Product_Rating'] = product_rating
            items['Product_Image'] = product_image
            items['Product_URL'] = ['amazon.com' + product_url[0]]
            items['Number_Of_Ratings'] = number_of_ratings

            yield items

        next_page = response.css('a.s-pagination-item::attr(href)').get()

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

