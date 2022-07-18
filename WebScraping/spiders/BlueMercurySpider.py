import scrapy
from scrapy.crawler import CrawlerProcess
from ..items import WebscrapingItem
import os
import requests
from time import sleep
from random import randint


class BlueMercurySpider(scrapy.Spider):
    name = 'BlueMercury'
    items = WebscrapingItem()

    start_urls = ['https://bluemercury.com/collections/hair']

    # path_to_file = os.path.join(os.path.dirname(__file__), 'blueMercury.txt')
    # with open(path_to_file, 'r') as file:
    #     start_urls = [line.strip() for line in file]

    def parse(self, response):
        blue_mercury_beauty = {}
        cc = 0
        page = 2

        the_url = response.request.url
        url_ = the_url.strip()
        cc += 1
        category_name = url_.split('/')[-1]

        print(cc, '**** SCRAPING CATEGORY: ', category_name)
        category_name_dict = {}

        # for page in range(1, 2):
        #     # (1, 100):

        def total_products_in_cat(url):
            headers = {
                'authority': 'bluemercury.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                # Requests sorts cookies= alphabetically
                'cookie': '_vuid=50575891-8427-4111-bcb8-2c67bb455211; secure_customer_sig=; localization=US; '
                          '_orig_referrer=https%3A%2F%2Fwww.upwork.com%2F; _landing_page=%2F; '
                          '_y=bd6c7c7e-f7e7-4a2c-b939-ad75562d64dc; _shopify_y=bd6c7c7e-f7e7-4a2c-b939-ad75562d64dc; '
                          '_tracking_consent=%7B%22reg%22%3A%22%22%2C%22v%22%3A%222.0%22%2C%22con%22%3A%7B%22GDPR%22'
                          '%3A%22%22%7D%2C%22lim%22%3A%5B%22CCPA_BLOCK_ALL%22%2C%22GDPR%22%5D%7D; _shopify_tw=; '
                          '_shopify_m=persistent; ku1-vid=ee0019fe-5b86-0d32-32ab-640620861548; '
                          '_mibhv=anon-1651613394151-2417647208_6425; BVBRANDID=5d89aee1-b19d-45c4-aeb5-ac4637d7766e; '
                          'swym-pid="FX2uiw+c1GfrGxB8/Pw1W3f9WFPfCiQgOVX6kwSA0wY="; '
                          '_gcl_au=1.1.2093848782.1651613397; '
                          'swym-swymRegid'
                          '="QvSbwC2Sa7G4HqMJOveQadIafR5jH96IHBKefrqXvmuk9v0zlNKgAawUuDx5REjEvsr_0eMUKqNEsK92vD2c3kuzDqT_0CX-rAF-GZRgnCu7C0E2CGuC3hHKGo8xG2JmGPLUmCqer-MfpQZQeLhI9PBXZMmGdm_XMifUxzHyRx4"; swym-email=null; _bamls_usid=3bbb840e-af1b-4c4c-ba2a-2b21870c6c4e; swym-cu_ct=undefined; GSIDITPmVMzaL4E1=ed92ad6b-1af3-4247-9098-db2bbe578064; STSIDITPmVMzaL4E1=8e3336e2-2966-4a30-9483-829c1b20ef9d; _pin_unauth=dWlkPU5tSTBObU0zTTJNdE5tVXhaUzAwWVRSa0xXRTNOelV0TTJOaFptVmhaVFF4TkRZeQ; ltkpopup-suppression-82ba628a-4ed4-44da-981c-e9c9100839e3=1; _hjSessionUser_2095881=eyJpZCI6ImRhMDU3NzZjLTRkZTYtNTRlMS04YzJmLWU0Nzk1MmI5MmUxNiIsImNyZWF0ZWQiOjE2NTE2MTM0MDA5NjcsImV4aXN0aW5nIjp0cnVlfQ==; truyoConsent={}; rskxRunCookie=0; rCookie=5wlbni0we8nlr69uksjmal2qnzzfi; _shg_user_id=530b86ad-11ab-452b-ab76-01c5a0e04f5f; rmStore=dmid:false|amid:43420|smid:9a709236-a0b9-4a4e-a626-7728b4493dea; swym-instrumentMap={}; ku1-sid=1v9_XxetcnUE_CV44-Km9; ltkSubscriber-Header=eyJsdGtDaGFubmVsIjoiZW1haWwiLCJsdGtUcmlnZ2VyIjoibG9hZCJ9; ltkSubscriber-Footer=eyJsdGtDaGFubmVsIjoiZW1haWwiLCJsdGtUcmlnZ2VyIjoibG9hZCJ9; _gid=GA1.2.1938613967.1652042782; XsellHiPerHistory=3#; ltkpopup-session-depth=1-4; ltkSubscriber-Footer - New=eyJsdGtDaGFubmVsIjoiZW1haWwiLCJsdGtUcmlnZ2VyIjoibG9hZCIsImx0a0VtYWlsIjoiIn0%3D; nxtck-identity-mgmt=1; _s=aa4cb6d5-4094-40C5-7625-04C4BE162C81; _shopify_s=aa4cb6d5-4094-40C5-7625-04C4BE162C81; _shopify_sa_p=; swym-session-id="x5z4hrc462hxzzkentq7rva7rrwm7d3ovpwppz4tdrdjtw4nn59i6dk4of26ocee"; swym-o_s=true; _shopify_tm=; XsellHiPerRef=https%3A%2F%2Fbluemercury.com%2Fcollections%2Fmakeup%20; XsellHiPerUserAlias=%23; XsellHiPerVisit=2#1652042784; rr_rcs=eF5j4cotK8lMETC0MDPVNdQ1ZClN9kg1NUs1M7M007U0NTDTNTFITtI1NzWz1DWxNDMwMkozTktKNgUAhbMNww; BVBRANDSID=332ae72b-b670-420f-b172-ccbde1853851; _hjIncludedInSessionSample=0; _hjSession_2095881=eyJpZCI6IjAyZDE0MDhjLTZkODktNDBlNC1hOWI2LWZhMDIwNjEyZjYwMyIsImNyZWF0ZWQiOjE2NTIxMjQ2MDcwODEsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _clck=xam7tk|1|f1b|0; _shg_session_id=1c2c6801-6063-4db8-975c-7f073bda08d3; lastRskxRun=1652124615028; cto_bundle=wjoEmV9CMFNCWGYzR3ZsM0F5OUNrdEVtSHpZYXR5eHR1Y2x0N3BoQ0xHdUhtTEp1RzZPR3YzbklZdCUyQjd3NnNJYkpWJTJCS0ZwVDQ1UjR6dVZ5cGhSJTJGdXR2RDEybXY2SDdTNGZHN2JYOCUyQiUyRkhrcllEeUE4a1h2d3hkOHJOc0dtJTJGWVd5WnNoTGRnbFFtRkdFUm9jUjZuRzVXMHglMkJmQSUzRCUzRA; XsellHiPerAgentAvatar=; XsellHiPerChatWindow=%7C0%7C; XsellHiPerNoProactiveChat=no; _clsk=1b068d5|1652124684976|2|1|l.clarity.ms/collect; _shopify_sa_t=2022-05-09T19%3A33%3A06.764Z; _ga_4KL76R32P5=GS1.1.1652124598.6.1.1652124788.0; _ga=GA1.2.1099441137.1651613392; _gat=1; _gat_UA-2217560-1=1; _uetsid=ed7e7480cf0f11ec859a6d7910815d65; _uetvid=2dcee970cb2811ecafda5db1d4272fb2',
                'referer': f'{url}',
                'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Microsoft Edge";v="101"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32',
            }
            params = {
                # 'page': f'{page}',
                'view': 'json',
                # 'sort_by': 'best-selling',
            }
            session = requests.Session()

            response_ = session.get(f'{url}', params=params, headers=headers)
            return len(response_.json()), response_

        total_products, response = total_products_in_cat(url_)

        def scrape_products_from_response(response_, category_name):
            headers = {
                'authority': 'bluemercury.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                # Requests sorts cookies= alphabetically
                'cookie': '_vuid=50575891-8427-4111-bcb8-2c67bb455211; secure_customer_sig=; localization=US; _orig_referrer=https%3A%2F%2Fwww.upwork.com%2F; _landing_page=%2F; _y=bd6c7c7e-f7e7-4a2c-b939-ad75562d64dc; _shopify_y=bd6c7c7e-f7e7-4a2c-b939-ad75562d64dc; _tracking_consent=%7B%22reg%22%3A%22%22%2C%22v%22%3A%222.0%22%2C%22con%22%3A%7B%22GDPR%22%3A%22%22%7D%2C%22lim%22%3A%5B%22CCPA_BLOCK_ALL%22%2C%22GDPR%22%5D%7D; _shopify_tw=; _shopify_m=persistent; ku1-vid=ee0019fe-5b86-0d32-32ab-640620861548; _mibhv=anon-1651613394151-2417647208_6425; BVBRANDID=5d89aee1-b19d-45c4-aeb5-ac4637d7766e; swym-pid="FX2uiw+c1GfrGxB8/Pw1W3f9WFPfCiQgOVX6kwSA0wY="; _gcl_au=1.1.2093848782.1651613397; swym-swymRegid="QvSbwC2Sa7G4HqMJOveQadIafR5jH96IHBKefrqXvmuk9v0zlNKgAawUuDx5REjEvsr_0eMUKqNEsK92vD2c3kuzDqT_0CX-rAF-GZRgnCu7C0E2CGuC3hHKGo8xG2JmGPLUmCqer-MfpQZQeLhI9PBXZMmGdm_XMifUxzHyRx4"; swym-email=null; _bamls_usid=3bbb840e-af1b-4c4c-ba2a-2b21870c6c4e; swym-cu_ct=undefined; GSIDITPmVMzaL4E1=ed92ad6b-1af3-4247-9098-db2bbe578064; STSIDITPmVMzaL4E1=8e3336e2-2966-4a30-9483-829c1b20ef9d; _pin_unauth=dWlkPU5tSTBObU0zTTJNdE5tVXhaUzAwWVRSa0xXRTNOelV0TTJOaFptVmhaVFF4TkRZeQ; ltkpopup-suppression-82ba628a-4ed4-44da-981c-e9c9100839e3=1; _hjSessionUser_2095881=eyJpZCI6ImRhMDU3NzZjLTRkZTYtNTRlMS04YzJmLWU0Nzk1MmI5MmUxNiIsImNyZWF0ZWQiOjE2NTE2MTM0MDA5NjcsImV4aXN0aW5nIjp0cnVlfQ==; truyoConsent={}; rskxRunCookie=0; rCookie=5wlbni0we8nlr69uksjmal2qnzzfi; _shg_user_id=530b86ad-11ab-452b-ab76-01c5a0e04f5f; rmStore=dmid:false|amid:43420|smid:9a709236-a0b9-4a4e-a626-7728b4493dea; swym-instrumentMap={}; ku1-sid=1v9_XxetcnUE_CV44-Km9; ltkSubscriber-Header=eyJsdGtDaGFubmVsIjoiZW1haWwiLCJsdGtUcmlnZ2VyIjoibG9hZCJ9; ltkSubscriber-Footer=eyJsdGtDaGFubmVsIjoiZW1haWwiLCJsdGtUcmlnZ2VyIjoibG9hZCJ9; _gid=GA1.2.1938613967.1652042782; XsellHiPerHistory=3#; ltkpopup-session-depth=1-4; ltkSubscriber-Footer - New=eyJsdGtDaGFubmVsIjoiZW1haWwiLCJsdGtUcmlnZ2VyIjoibG9hZCIsImx0a0VtYWlsIjoiIn0%3D; nxtck-identity-mgmt=1; _s=aa4cb6d5-4094-40C5-7625-04C4BE162C81; _shopify_s=aa4cb6d5-4094-40C5-7625-04C4BE162C81; _shopify_sa_p=; swym-session-id="x5z4hrc462hxzzkentq7rva7rrwm7d3ovpwppz4tdrdjtw4nn59i6dk4of26ocee"; swym-o_s=true; _shopify_tm=; XsellHiPerRef=https%3A%2F%2Fbluemercury.com%2Fcollections%2Fmakeup%20; XsellHiPerUserAlias=%23; XsellHiPerVisit=2#1652042784; rr_rcs=eF5j4cotK8lMETC0MDPVNdQ1ZClN9kg1NUs1M7M007U0NTDTNTFITtI1NzWz1DWxNDMwMkozTktKNgUAhbMNww; BVBRANDSID=332ae72b-b670-420f-b172-ccbde1853851; _hjIncludedInSessionSample=0; _hjSession_2095881=eyJpZCI6IjAyZDE0MDhjLTZkODktNDBlNC1hOWI2LWZhMDIwNjEyZjYwMyIsImNyZWF0ZWQiOjE2NTIxMjQ2MDcwODEsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _clck=xam7tk|1|f1b|0; _shg_session_id=1c2c6801-6063-4db8-975c-7f073bda08d3; lastRskxRun=1652124615028; cto_bundle=wjoEmV9CMFNCWGYzR3ZsM0F5OUNrdEVtSHpZYXR5eHR1Y2x0N3BoQ0xHdUhtTEp1RzZPR3YzbklZdCUyQjd3NnNJYkpWJTJCS0ZwVDQ1UjR6dVZ5cGhSJTJGdXR2RDEybXY2SDdTNGZHN2JYOCUyQiUyRkhrcllEeUE4a1h2d3hkOHJOc0dtJTJGWVd5WnNoTGRnbFFtRkdFUm9jUjZuRzVXMHglMkJmQSUzRCUzRA; XsellHiPerAgentAvatar=; XsellHiPerChatWindow=%7C0%7C; XsellHiPerNoProactiveChat=no; _clsk=1b068d5|1652124684976|2|1|l.clarity.ms/collect; _shopify_sa_t=2022-05-09T19%3A33%3A06.764Z; _ga_4KL76R32P5=GS1.1.1652124598.6.1.1652124788.0; _ga=GA1.2.1099441137.1651613392; _gat=1; _gat_UA-2217560-1=1; _uetsid=ed7e7480cf0f11ec859a6d7910815d65; _uetvid=2dcee970cb2811ecafda5db1d4272fb2',
                'referer': f'{url_}',
                'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Microsoft Edge";v="101"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32',
            }

            items = WebscrapingItem()

            if response_:
                for pc in range(len(response_.json())):
                    product = response_.json()[pc]
                    product_dict = {}
                    product_id = product['id']
                    product_category = category_name
                    product_name = product['title']
                    product_url = f'https://bluemercury.com{product["url_"]}'
                    product_img = ''
                    try:
                        product_img = product['images'][0]['src']
                        if 'http' not in product_img:
                            product_img = f'https:{product_img}'
                    except:
                        pass

                        print('*' * 3, pc, '*' * 3)
                        print(f'Product ID:', product_id)
                        print(f'Product Name:', product_name)

                        offset = 0
                        rc = 0
                        params_raw = {
                            'Filter': f'ProductId:{product_id}',
                            'Sort': 'SubmissionTime:desc',
                            'Limit': '1000',
                            'Offset': f'{offset}',
                            'Include': 'Products,Comments',
                            'Stats': 'Reviews',
                            'passkey': 'cahurH4YTLYFW0G5tMOsmjT7mau3DH0bwAqogWpgsB0SU',
                            'apiversion': '5.4',
                        }
                        reviews_raw = requests.get('https://api.bazaarvoice.com/data/reviews.json',
                                                   params=params_raw)
                        total_results = reviews_raw.json()['TotalResults']
                        average_rating = ''
                        try:
                            average_rating = \
                                reviews_raw.json()['Includes']['Products'][f'{product_id}'][
                                    'ReviewStatistics']['AverageOverallRating']
                        except:
                            pass

                        # product_dict['No.'] = pc
                        product_dict['Product_ID'] = product_id
                        product_dict['Product_Name'] = product_name
                        product_dict['Product_Url'] = product_url
                        product_dict['Image'] = product_img
                        product_dict['Total_Reviews'] = total_results
                        product_dict['Avg_Rating'] = average_rating
                        product_dict['product_category'] = product_category

                        print('---> TOTAL REVIEWS FOR THIS PRODUCT ARE', total_results)
                        for count in range(0, int(int(total_results) / 100) + 1):
                            offset = count * 100
                            params = {
                                'Filter': f'ProductId:{product_id}',
                                'Sort': 'SubmissionTime:desc',
                                'Limit': '300',
                                'Offset': f'{offset}',
                                'Include': 'Products,Comments',
                                'Stats': 'Reviews',
                                'passkey': 'cahurH4YTLYFW0G5tMOsmjT7mau3DH0bwAqogWpgsB0SU',
                                'apiversion': '5.4',
                            }

                            sleep_time = randint(2, 5)
                            print('---> Sleeping for', sleep_time)
                            if total_results != 0:
                                sleep(sleep_time)

                            reviews_dict = {}
                            reviews_res = requests.get('https://api.bazaarvoice.com/data/reviews.json',
                                                       params=params)
                            reviews = reviews_res.json()['Results']

                            for review in reviews:
                                rc += 1
                                author_name = review['UserNickname']
                                rating = review['Rating']
                                author_id = review['Id']
                                title = review['Title']
                                review_text = review['ReviewText']

                                reviews_dict['No.'] = rc
                                reviews_dict['Product_ID'] = product_id
                                reviews_dict['Product_Name'] = product_name
                                reviews_dict['Author_ID'] = author_id
                                reviews_dict['Author_Name'] = author_name
                                reviews_dict['Rating'] = rating
                                reviews_dict['Title'] = title
                                reviews_dict['ReviewText'] = review_text

                                print(f'--> Got total reviews {rc}')

                            product_dict[f'{product_name}_reviews'] = reviews_dict

                            items['Product_Category'] = category_name
                            # items['Product_Category'] = product_category
                            items['Product_Name'] = product_name
                            # items['Product_Price'] = product_price
                            items['Product_Rating'] = average_rating
                            items['Product_Image'] = product_img
                            items['Product_URL'] = product_url  # ['amazon.com' + product_url[0]]
                            items['Number_Of_Ratings'] = total_results
                            items['Product_ID'] = product_id

                        category_name_dict[product_name] = product_dict

                    scrape_products_from_response(response_, category_name)

        # try:
        #     h = httplib2.Http()
        #     next_page = the_url + '?pg=' + str(page)
        #     check = h.request(next_page, 'HEAD')
        # check = requests.get(next_page)
        # page_check = httplib2.HTTPConnection(next_page)
        # page_check.request

        #     if assert int(check[0]['status']) < 400:
        #         print('**** GOING TO NEXT PAGE')
        #         page += 1
        #         yield check.follow(next_page, callback=self.parse)
        #     else:
        #         print('**** END OF CATEGORY')
        #         # break
        # except:
        #     break

        blue_mercury_beauty[category_name] = category_name_dict


if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(BlueMercurySpider)
    process.start()
