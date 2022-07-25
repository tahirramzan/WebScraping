import scrapy
import self as self
from scrapy.crawler import CrawlerProcess
from ..items import WebsiteCategories
from ..scraperFunction import scrape_products_from_response
import requests
from time import sleep
from random import randint


class BlueMercurySpider(scrapy.Spider):
    name = 'blue_Mercury'
    start_urls = ['https://bluemercury.com/collections/hair']

    def parse(self, response):

        cat_dict = WebsiteCategories()
        cc = 0
        # page = 2

        url = response.request.url.strip()
        cc += 1
        category_name = url.split('/')[-1]

        print(cc, '**** SCRAPING CATEGORY: ', category_name)

        if category_name == 'bath-body':
            cat_name = 'body'
        elif category_name == 'tools-accessories':
            cat_name = 'tools_accessories'
        elif category_name == 'for-men':
            cat_name = 'men'
        elif category_name == 'best-sellers':
            cat_name = 'best_sellers'
        else:
            cat_name = category_name

        for page in range(1, 2):
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

                return len(response.json()), response

            total_products, response = total_products_in_cat(url, page)

        cat_dict[f'{cat_name}'] = scrape_products_from_response(response, cat_name)

        yield cat_dict

