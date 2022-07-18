import json

import scrapy
from ..items import WebscrapingItem
import os
import pathlib
import requests
from time import sleep
from random import randint
from bs4 import BeautifulSoup as bs


class BlueMercurySpider(scrapy.Spider):
    name = 'BlueMercury'
    items = WebscrapingItem()

    start_urls = [
        # 'https://bluemercury.com/collections/makeup',
        # 'https://bluemercury.com/collections/hair',
        # 'https://bluemercury.com/collections/bath-body',
        # 'https://bluemercury.com/collections/fragrances',
        # 'https://bluemercury.com/collections/tools-accessories',
        # 'https://bluemercury.com/collections/home',
        # 'https://bluemercury.com/collections/suncare',
        # 'https://bluemercury.com/collections/for-men',
        # 'https://bluemercury.com/collections/gifts',
        # 'https://bluemercury.com/collections/best-sellers'
    ]

    def parse(self, response):

        blue_mercury_beauty = {}
        cc = 0

        path_to_file = os.path.join(os.path.dirname(__file__), 'blueMercury.txt')
        with open(path_to_file, 'r') as ff:
            for line in start_urls:
                # url = start_urls
                url = line.strip()
                cc += 1
                # url = start_urls
                print(cc, '**** SCRAPING CATEGORY: ', url)

                category_name = url.split('/')[-1]
                # category_name_to_save = pathlib.Path(category_name)
                # category_name_to_save.mkdir(parents=True, exist_ok=True)

                category_name_dict = {}

                for page in range(1, 2):
                    # (1, 100):

                    def total_products_in_cat(url, page):
                        headers = {
                            'authority': 'bluemercury.com',
                            'accept': '*/*',
                            'accept-language': 'en-US,en;q=0.9',
                            # Requests sorts cookies= alphabetically
                            'cookie': '_vuid=50575891-8427-4111-bcb8-2c67bb455211; secure_customer_sig=; localization=US; _orig_referrer=https%3A%2F%2Fwww.upwork.com%2F; _landing_page=%2F; _y=bd6c7c7e-f7e7-4a2c-b939-ad75562d64dc; _shopify_y=bd6c7c7e-f7e7-4a2c-b939-ad75562d64dc; _tracking_consent=%7B%22reg%22%3A%22%22%2C%22v%22%3A%222.0%22%2C%22con%22%3A%7B%22GDPR%22%3A%22%22%7D%2C%22lim%22%3A%5B%22CCPA_BLOCK_ALL%22%2C%22GDPR%22%5D%7D; _shopify_tw=; _shopify_m=persistent; ku1-vid=ee0019fe-5b86-0d32-32ab-640620861548; _mibhv=anon-1651613394151-2417647208_6425; BVBRANDID=5d89aee1-b19d-45c4-aeb5-ac4637d7766e; swym-pid="FX2uiw+c1GfrGxB8/Pw1W3f9WFPfCiQgOVX6kwSA0wY="; _gcl_au=1.1.2093848782.1651613397; swym-swymRegid="QvSbwC2Sa7G4HqMJOveQadIafR5jH96IHBKefrqXvmuk9v0zlNKgAawUuDx5REjEvsr_0eMUKqNEsK92vD2c3kuzDqT_0CX-rAF-GZRgnCu7C0E2CGuC3hHKGo8xG2JmGPLUmCqer-MfpQZQeLhI9PBXZMmGdm_XMifUxzHyRx4"; swym-email=null; _bamls_usid=3bbb840e-af1b-4c4c-ba2a-2b21870c6c4e; swym-cu_ct=undefined; GSIDITPmVMzaL4E1=ed92ad6b-1af3-4247-9098-db2bbe578064; STSIDITPmVMzaL4E1=8e3336e2-2966-4a30-9483-829c1b20ef9d; _pin_unauth=dWlkPU5tSTBObU0zTTJNdE5tVXhaUzAwWVRSa0xXRTNOelV0TTJOaFptVmhaVFF4TkRZeQ; ltkpopup-suppression-82ba628a-4ed4-44da-981c-e9c9100839e3=1; _hjSessionUser_2095881=eyJpZCI6ImRhMDU3NzZjLTRkZTYtNTRlMS04YzJmLWU0Nzk1MmI5MmUxNiIsImNyZWF0ZWQiOjE2NTE2MTM0MDA5NjcsImV4aXN0aW5nIjp0cnVlfQ==; truyoConsent={}; rskxRunCookie=0; rCookie=5wlbni0we8nlr69uksjmal2qnzzfi; _shg_user_id=530b86ad-11ab-452b-ab76-01c5a0e04f5f; rmStore=dmid:false|amid:43420|smid:9a709236-a0b9-4a4e-a626-7728b4493dea; swym-instrumentMap={}; ku1-sid=1v9_XxetcnUE_CV44-Km9; ltkSubscriber-Header=eyJsdGtDaGFubmVsIjoiZW1haWwiLCJsdGtUcmlnZ2VyIjoibG9hZCJ9; ltkSubscriber-Footer=eyJsdGtDaGFubmVsIjoiZW1haWwiLCJsdGtUcmlnZ2VyIjoibG9hZCJ9; _gid=GA1.2.1938613967.1652042782; XsellHiPerHistory=3#; ltkpopup-session-depth=1-4; ltkSubscriber-Footer - New=eyJsdGtDaGFubmVsIjoiZW1haWwiLCJsdGtUcmlnZ2VyIjoibG9hZCIsImx0a0VtYWlsIjoiIn0%3D; nxtck-identity-mgmt=1; _s=aa4cb6d5-4094-40C5-7625-04C4BE162C81; _shopify_s=aa4cb6d5-4094-40C5-7625-04C4BE162C81; _shopify_sa_p=; swym-session-id="x5z4hrc462hxzzkentq7rva7rrwm7d3ovpwppz4tdrdjtw4nn59i6dk4of26ocee"; swym-o_s=true; _shopify_tm=; XsellHiPerRef=https%3A%2F%2Fbluemercury.com%2Fcollections%2Fmakeup%20; XsellHiPerUserAlias=%23; XsellHiPerVisit=2#1652042784; rr_rcs=eF5j4cotK8lMETC0MDPVNdQ1ZClN9kg1NUs1M7M007U0NTDTNTFITtI1NzWz1DWxNDMwMkozTktKNgUAhbMNww; BVBRANDSID=332ae72b-b670-420f-b172-ccbde1853851; _hjIncludedInSessionSample=0; _hjSession_2095881=eyJpZCI6IjAyZDE0MDhjLTZkODktNDBlNC1hOWI2LWZhMDIwNjEyZjYwMyIsImNyZWF0ZWQiOjE2NTIxMjQ2MDcwODEsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _clck=xam7tk|1|f1b|0; _shg_session_id=1c2c6801-6063-4db8-975c-7f073bda08d3; lastRskxRun=1652124615028; cto_bundle=wjoEmV9CMFNCWGYzR3ZsM0F5OUNrdEVtSHpZYXR5eHR1Y2x0N3BoQ0xHdUhtTEp1RzZPR3YzbklZdCUyQjd3NnNJYkpWJTJCS0ZwVDQ1UjR6dVZ5cGhSJTJGdXR2RDEybXY2SDdTNGZHN2JYOCUyQiUyRkhrcllEeUE4a1h2d3hkOHJOc0dtJTJGWVd5WnNoTGRnbFFtRkdFUm9jUjZuRzVXMHglMkJmQSUzRCUzRA; XsellHiPerAgentAvatar=; XsellHiPerChatWindow=%7C0%7C; XsellHiPerNoProactiveChat=no; _clsk=1b068d5|1652124684976|2|1|l.clarity.ms/collect; _shopify_sa_t=2022-05-09T19%3A33%3A06.764Z; _ga_4KL76R32P5=GS1.1.1652124598.6.1.1652124788.0; _ga=GA1.2.1099441137.1651613392; _gat=1; _gat_UA-2217560-1=1; _uetsid=ed7e7480cf0f11ec859a6d7910815d65; _uetvid=2dcee970cb2811ecafda5db1d4272fb2',
                            'referer': f'{url}',
                            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Microsoft Edge";v="101"',
                            'sec-ch-ua-mobile': '?0',
                            'sec-ch-ua-platform': '"Windows"',
                            'sec-fetch-dest': 'empty',
                            'sec-fetch-mode': 'cors',
                            'sec-fetch-site': 'same-origin',
                            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32',
                        }
                        params = {
                            'page': f'{page}',
                            'view': 'json',
                            # 'sort_by': 'best-selling',
                        }
                        session = requests.Session()

                        response = session.get(f'{url}', params=params, headers=headers)
                        return (len(response.json()), response)

                    total_products, response = total_products_in_cat(url, page)

                    def scrape_products_from_response(response, category_name):
                        headers = {
                            'authority': 'bluemercury.com',
                            'accept': '*/*',
                            'accept-language': 'en-US,en;q=0.9',
                            # Requests sorts cookies= alphabetically
                            'cookie': '_vuid=50575891-8427-4111-bcb8-2c67bb455211; secure_customer_sig=; localization=US; _orig_referrer=https%3A%2F%2Fwww.upwork.com%2F; _landing_page=%2F; _y=bd6c7c7e-f7e7-4a2c-b939-ad75562d64dc; _shopify_y=bd6c7c7e-f7e7-4a2c-b939-ad75562d64dc; _tracking_consent=%7B%22reg%22%3A%22%22%2C%22v%22%3A%222.0%22%2C%22con%22%3A%7B%22GDPR%22%3A%22%22%7D%2C%22lim%22%3A%5B%22CCPA_BLOCK_ALL%22%2C%22GDPR%22%5D%7D; _shopify_tw=; _shopify_m=persistent; ku1-vid=ee0019fe-5b86-0d32-32ab-640620861548; _mibhv=anon-1651613394151-2417647208_6425; BVBRANDID=5d89aee1-b19d-45c4-aeb5-ac4637d7766e; swym-pid="FX2uiw+c1GfrGxB8/Pw1W3f9WFPfCiQgOVX6kwSA0wY="; _gcl_au=1.1.2093848782.1651613397; swym-swymRegid="QvSbwC2Sa7G4HqMJOveQadIafR5jH96IHBKefrqXvmuk9v0zlNKgAawUuDx5REjEvsr_0eMUKqNEsK92vD2c3kuzDqT_0CX-rAF-GZRgnCu7C0E2CGuC3hHKGo8xG2JmGPLUmCqer-MfpQZQeLhI9PBXZMmGdm_XMifUxzHyRx4"; swym-email=null; _bamls_usid=3bbb840e-af1b-4c4c-ba2a-2b21870c6c4e; swym-cu_ct=undefined; GSIDITPmVMzaL4E1=ed92ad6b-1af3-4247-9098-db2bbe578064; STSIDITPmVMzaL4E1=8e3336e2-2966-4a30-9483-829c1b20ef9d; _pin_unauth=dWlkPU5tSTBObU0zTTJNdE5tVXhaUzAwWVRSa0xXRTNOelV0TTJOaFptVmhaVFF4TkRZeQ; ltkpopup-suppression-82ba628a-4ed4-44da-981c-e9c9100839e3=1; _hjSessionUser_2095881=eyJpZCI6ImRhMDU3NzZjLTRkZTYtNTRlMS04YzJmLWU0Nzk1MmI5MmUxNiIsImNyZWF0ZWQiOjE2NTE2MTM0MDA5NjcsImV4aXN0aW5nIjp0cnVlfQ==; truyoConsent={}; rskxRunCookie=0; rCookie=5wlbni0we8nlr69uksjmal2qnzzfi; _shg_user_id=530b86ad-11ab-452b-ab76-01c5a0e04f5f; rmStore=dmid:false|amid:43420|smid:9a709236-a0b9-4a4e-a626-7728b4493dea; swym-instrumentMap={}; ku1-sid=1v9_XxetcnUE_CV44-Km9; ltkSubscriber-Header=eyJsdGtDaGFubmVsIjoiZW1haWwiLCJsdGtUcmlnZ2VyIjoibG9hZCJ9; ltkSubscriber-Footer=eyJsdGtDaGFubmVsIjoiZW1haWwiLCJsdGtUcmlnZ2VyIjoibG9hZCJ9; _gid=GA1.2.1938613967.1652042782; XsellHiPerHistory=3#; ltkpopup-session-depth=1-4; ltkSubscriber-Footer - New=eyJsdGtDaGFubmVsIjoiZW1haWwiLCJsdGtUcmlnZ2VyIjoibG9hZCIsImx0a0VtYWlsIjoiIn0%3D; nxtck-identity-mgmt=1; _s=aa4cb6d5-4094-40C5-7625-04C4BE162C81; _shopify_s=aa4cb6d5-4094-40C5-7625-04C4BE162C81; _shopify_sa_p=; swym-session-id="x5z4hrc462hxzzkentq7rva7rrwm7d3ovpwppz4tdrdjtw4nn59i6dk4of26ocee"; swym-o_s=true; _shopify_tm=; XsellHiPerRef=https%3A%2F%2Fbluemercury.com%2Fcollections%2Fmakeup%20; XsellHiPerUserAlias=%23; XsellHiPerVisit=2#1652042784; rr_rcs=eF5j4cotK8lMETC0MDPVNdQ1ZClN9kg1NUs1M7M007U0NTDTNTFITtI1NzWz1DWxNDMwMkozTktKNgUAhbMNww; BVBRANDSID=332ae72b-b670-420f-b172-ccbde1853851; _hjIncludedInSessionSample=0; _hjSession_2095881=eyJpZCI6IjAyZDE0MDhjLTZkODktNDBlNC1hOWI2LWZhMDIwNjEyZjYwMyIsImNyZWF0ZWQiOjE2NTIxMjQ2MDcwODEsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _clck=xam7tk|1|f1b|0; _shg_session_id=1c2c6801-6063-4db8-975c-7f073bda08d3; lastRskxRun=1652124615028; cto_bundle=wjoEmV9CMFNCWGYzR3ZsM0F5OUNrdEVtSHpZYXR5eHR1Y2x0N3BoQ0xHdUhtTEp1RzZPR3YzbklZdCUyQjd3NnNJYkpWJTJCS0ZwVDQ1UjR6dVZ5cGhSJTJGdXR2RDEybXY2SDdTNGZHN2JYOCUyQiUyRkhrcllEeUE4a1h2d3hkOHJOc0dtJTJGWVd5WnNoTGRnbFFtRkdFUm9jUjZuRzVXMHglMkJmQSUzRCUzRA; XsellHiPerAgentAvatar=; XsellHiPerChatWindow=%7C0%7C; XsellHiPerNoProactiveChat=no; _clsk=1b068d5|1652124684976|2|1|l.clarity.ms/collect; _shopify_sa_t=2022-05-09T19%3A33%3A06.764Z; _ga_4KL76R32P5=GS1.1.1652124598.6.1.1652124788.0; _ga=GA1.2.1099441137.1651613392; _gat=1; _gat_UA-2217560-1=1; _uetsid=ed7e7480cf0f11ec859a6d7910815d65; _uetvid=2dcee970cb2811ecafda5db1d4272fb2',
                            'referer': f'{url}',
                            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Microsoft Edge";v="101"',
                            'sec-ch-ua-mobile': '?0',
                            'sec-ch-ua-platform': '"Windows"',
                            'sec-fetch-dest': 'empty',
                            'sec-fetch-mode': 'cors',
                            'sec-fetch-site': 'same-origin',
                            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32',
                        }

                        items = WebscrapingItem()

                        if response:
                            for pc in range(len(response.json())):
                                product = response.json()[pc]
                                product_dict = {}
                                product_id = product['id']
                                product_category = category_name
                                product_name = product['title']
                                product_url = f'https://bluemercury.com{product["url"]}'
                                product_img = ''
                                try:
                                    product_img = product['images'][0]['src']
                                    if 'http' not in product_img:
                                        product_img = f'https:{product_img}'
                                except:
                                    pass

                                    # product_dir = f"{dir_name}\\{product_id}"
                                    # try:
                                    #     os.mkdir(product_dir)
                                    # except:
                                    #     print('######## this product is already scraped once ########')
                                    #     continue
                                    # img_dir = f"{dir_name}\\{product_id}\\{product_id}.jpg"
                                    # if product_img:
                                    #     img_data = requests.get(product_img,headers=headers,stream=True)
                                    # with open(img_dir, 'wb') as f:
                                    #     f.write(img_data.content)

                                    # product_csv_dir = f"{product_dir}\\{product_id}.csv"
                                    # reviews_csv_dir = f"{product_dir}\\{product_id}-reviews.csv"

                                    print('*' * 3, pc, '*' * 3)
                                    print(f'Product ID:', product_id)
                                    print(f'Product Name:', product_name)

                                    # p_firstrow = ['No.', 'Product ID', 'Product Name', 'Product Url','Image','Total Reviews','Avg. Rating']
                                    # with open(f'{product_csv_dir}', 'a', newline='') as csvFile:
                                    #     writer = csv.writer(csvFile)
                                    #     writer.writerow(p_firstrow)
                                    #     csvFile.close()

                                    # r_firstrow = ['No.', 'Product ID', 'Product Name', 'Author ID', 'Author Name','Rating','Title', 'ReviewText']
                                    # with open(f'{reviews_csv_dir}', 'a', newline='') as csvFile:
                                    #     writer = csv.writer(csvFile)
                                    #     writer.writerow(r_firstrow)
                                    #     csvFile.close()

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
                                                'ReviewStatistics'][
                                                'AverageOverallRating']
                                    except:
                                        pass

                                    # p_row = [pc,product_id,product_name,product_url,product_img,total_results,average_rating]
                                    # with open(f'{product_dict}', 'a', newline='' , encoding='utf-8') as csvFile:
                                    #     writer = csv.writer(csvFile)
                                    #     writer.writerow(p_row)
                                    #     csvFile.close()
                                    # 'No.', 'Product_ID', 'Product_Name', 'Product_Url','Image','Total_Reviews','Avg_Rating'

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

                                        sleep_time = randint(1, 4)
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

                                            # r_row = [rc,product_id,product_name,author_id,author_name,rating,title,review_text]
                                            # with open(f'{reviews_dict}', 'a', newline='' , encoding='utf-8') as csvFile:
                                            #     writer = csv.writer(csvFile)
                                            #     writer.writerow(r_row)
                                            #     csvFile.close()
                                            # 'No.', 'Product_ID', 'Product_Name', 'Author_ID', 'Author_Name','Rating','Title', 'ReviewText'

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

                                        # items['Product_Category'] = 'Skincare'
                                        items['Product_Category'] = product_category
                                        items['Product_Name'] = product_name
                                        # items['Product_Price'] = product_price
                                        items['Product_Rating'] = average_rating
                                        items['Product_Image'] = product_img
                                        items['Product_URL'] = product_url  # ['amazon.com' + product_url[0]]
                                        items['Number_Of_Ratings'] = total_results
                                        items['Product_ID'] = product_id

                                    category_name_dict[product_name] = product_dict

                                scrape_products_from_response(response, category_name)

                                if (total_products < 1000):
                                    print('**** END OF CATEGORY')
                                    break
                                else:
                                    print('**** GOING TO NEXT PAGE')
                                    continue

                            blue_mercury_beauty[category_name] = category_name_dict

                            with open('blue_mercury_beauty_scrapped.json', 'w') as file:
                                json.dump(blue_mercury_beauty, file)
                                #     file.write(blue_mercury_beauty)
                                #     file.close()


# def parse(self, response):
#     all_products = response.css('div.s-main-slot')
#     items = WebscrapingItem()
#
#     for products in all_products:
#         product_name = products.css('h2.a-size-mini span.a-size-base-plus::text').extract()
#         product_price = products.css('span.a-offscreen::text').extract()
#         product_rating = products.css('span.a-icon-alt::text').extract()
#         product_image = products.css('div.a-section img.s-image::attr(src)').extract()
#         product_url = products.css('a.a-link-normal::attr(href)').extract()
#         number_of_ratings = products.css('span.a-size-base::text').extract()
#
#         #items['Product_Category'] = 'Skincare'
#         items['Product_Category'] = 'Make-Up'
#         items['Product_Name'] = product_name
#         items['Product_Price'] = product_price
#         items['Product_Rating'] = product_rating
#         items['Product_Image'] = product_image
#         items['Product_URL'] = ['amazon.com' + product_url[0]]
#         items['Number_Of_Ratings'] = number_of_ratings
#
#         yield items
#
#     next_page = response.css('a.s-pagination-item::attr(href)').get()
#
#     if next_page is not None:
#         yield response.follow(next_page, callback=self.parse)
