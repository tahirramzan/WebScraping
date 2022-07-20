import scrapy
from ..items import FullWebsite, WebsiteCategories, WebscrapingItem, DataHandler
from time import sleep
from random import randint


def review_handler(response, product_url, product_dict):
    response.follow(product_url)
    particular_prod = response.css('div.ProductRefreshed')
    product_dict['Product_Description'] = particular_prod.css('div.ProductInfo__Description::text')
    product_dict['Number_Of_Ratings'] = total_results = particular_prod.css('span.ReviewsSummary__NumReviews::text')
    product_dict['Product_Rating'] = particular_prod.css('div.Reviews__OverallRating::text')
    review_dict = DataHandler()

    try:
        all_reviews = particular_prod.css('div.Reviews__ReviewCards')
        for review in all_reviews:
            review_dict['Review_Author'] = review.css('spam.ReviewUser::text')
            review_dict['Review_Title'] = review.css('spam.ReviewTitle::text')
            review_dict['Review_Date'] = review.css('spam.ReviewDate::text')
            review_dict['Review_Text'] = review.css('spam.Whole ::text')

            sleep_time = randint(1, 4)
            print('---> Sleeping for', sleep_time)
            if total_results != 0:
                sleep(sleep_time)
    except:
        pass

    product_dict['Reviews'] = review_dict
    yield product_dict


def product_separator(all_products, cat_name):
    category_dict = WebsiteCategories()
    for product in all_products:
        product_dict = WebscrapingItem()
        product_dict['Product_Name'] = product.css('a.ProductCard__Title::text')
        product_dict['Product_URL'] = product_url = product.css('a.ProductCard__Title::attr(href')
        product_dict['Product_Price'] = product.css('div.ProductCard__Price::text')

        category_dict[f'{cat_name}'] = review_handler(product, product_url, product_dict)
        yield category_dict  # , product_title, product_url


class AmazonMakeupSpider(scrapy.Spider):
    name = 'BlueMercuryBot'
    start_urls = ['https://bluemercury.com/collections/hair']

    # the_url = start_urls

    def parse(self, response):

        url_ = response.request.url.strip()
        cat_name = url_.split('/')[-1]

        if cat_name == 'bath-body':
            cat_name = 'body'
        elif cat_name == 'tools-accessories':
            cat_name = 'tools_accessories'
        elif cat_name == 'for-men':
            cat_name = 'men'
        elif cat_name == 'best-sellers':
            cat_name = 'best_sellers'
        else:
            pass

        full_website = FullWebsite()
        all_products = response.css('div.CollectionsGrid__ProductCards')
        full_website[f'blue_mercury'] = product_separator(all_products, cat_name=cat_name)

        yield full_website
