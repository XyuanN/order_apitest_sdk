import requests


class OrderOid(object):
    def __init__(self, phone):
        self.phone = phone

    def get_pid(self):
        '''获取乘客账号的pid

            Args:
            phone (str): 线上乘客手机号

            Returns:
            pid: 手机号pid

        '''
        url = "https://didifarm.intra.xiaojukeji.com/beta/api/didifarm/v1/data/PhoneToUid/?dev=1&role=1&countryCode=86&phone="+str(self.phone)
        payload = {}
        headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'priority': 'u=1, i',
        'referer': 'https://didifarm.intra.xiaojukeji.com/passenger/phoneTouid',
        'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
        'Cookie': 'current_odin_platform=pc; SSO_AS_SUB_TICKET3114=24b0ae5cfb0b962c24382ad0d91821fe0003114000; SSO_AS_UID3114=elysianiu_i; _kylin_username=elysianiu_i; _kylin_username_zh=%E7%89%9B%E6%AD%86%E5%AA%9B; _OMGID=52c10386-731a-4c43-ab98-dbb017e433f8; _product_id=1; CASE_SSO_USERNAME=elysianiu_i; username=elysianiu_i; odin_jwt_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NTE3MDczMjAsImlhdCI6MTc0OTExNTMyMCwiaXNzIjoib2Rpbi54aWFvanVrZWppLmNvbSIsInN1YiI6ImVseXNpYW5pdV9pIn0.lGt7QwdzaiTSUMF3vYLL9TefEaNuAUgYtDhW7Vd0TZ8; ENG_prod_SESSION_ID=550e4448e899c4eef992ac626050fa73000915000; language=zh_CN; _kylin_ticket=ff67ccbb8e1925c5677393ac00dcc6940001268000; __hash__wa=20250611-didifarm-elysianiu_i-49ae4287-d298-4a9b-8ceb-82c80e3e29a4; __hash__cache=49ae4287-d298-4a9b-8ceb-82c80e3e29a4; user-fingerprint-water-mark=20250611-didifarm-elysianiu_i-49ae4287-d298-4a9b-8ceb-82c80e3e29a4'
        }
        response = requests.request("GET", url, headers=headers, json=payload)
        data = response.json()
        pid = data['data']['items'][0]['pid']
        return pid

    def get_low_oid(self, pid):
        '''获取低位订单号

            Args:
            pid (str): 线上乘客账号pid

            Returns:
            low_oid: 低位订单号

        '''
        url = "http://10.88.128.15:8000/dos/getPassengerHistoryOrderInfo"
        payload = "limit=%7B%22size%22%3A5%7D&passengerId="+str(pid)+"&fields=%5B%22order_id%22%2C%20%22district%22%5D&productId=0"
        headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        data = response.json()
        low_oid = data["data"][0]['order_id']
        return low_oid

    def get_high_oid(self, low_oid):
        '''获取高位订单号

            Args:
            low_oid (str): 低位订单号

            Returns:
            high_oid: 高位订单号

        '''
        url = "https://didifarm.intra.xiaojukeji.com/beta/api/didifarm/v1/data/transOid"
        payload = {
            "oid":low_oid,
            "district": "010",
            "action": "high"
        }
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'zh-CN,zh;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://didifarm.intra.xiaojukeji.com',
            'priority': 'u=1, i',
            'referer': 'https://didifarm.intra.xiaojukeji.com/order/transLowOid',
            'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
            'Cookie': 'current_odin_platform=pc; SSO_AS_SUB_TICKET3114=24b0ae5cfb0b962c24382ad0d91821fe0003114000; SSO_AS_UID3114=elysianiu_i; odin_jwt_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NTAzMzM2NTcsImlhdCI6MTc0Nzc0MTY1NywiaXNzIjoib2Rpbi54aWFvanVrZWppLmNvbSIsInN1YiI6ImVseXNpYW5pdV9pIn0.BVH9Yc2lBP9WNquwFLUwVicsa0C3x6UtDda-x8JMNkI; _kylin_username=elysianiu_i; _kylin_username_zh=%E7%89%9B%E6%AD%86%E5%AA%9B; _OMGID=52c10386-731a-4c43-ab98-dbb017e433f8; _product_id=1; CASE_SSO_USERNAME=elysianiu_i; username=elysianiu_i; ENG_prod_SESSION_ID=b2a19231ff9932e74341ffe01da5501a000915000; _kylin_ticket=99ac7e2b3ca0b6cc54662f4ff69894940001268000; __hash__wa=20250605-didifarm-elysianiu_i-adf808f8-afe6-4e48-9b5a-343192470e66; __hash__cache=adf808f8-afe6-4e48-9b5a-343192470e66; user-fingerprint-water-mark=20250605-didifarm-elysianiu_i-adf808f8-afe6-4e48-9b5a-343192470e66'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        data = response.json()
        high_oid = data["result"]["oid"]
        return high_oid
    
    def get_oid(self, low_oid):
        '''获取加密订单号

            Args:
            low_oid (str): 低位订单号

            Returns:
            oid: 加密订单号

        '''
        url = "https://didifarm.intra.xiaojukeji.com/beta/api/didifarm/v1/data/encodeOid"
        payload = {
            "oid":low_oid,
            "order_type":"0",
            "district":"010"
        }
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'zh-CN,zh;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://didifarm.intra.xiaojukeji.com',
            'priority': 'u=1, i',
            'referer': 'https://didifarm.intra.xiaojukeji.com/order/encodeOid',
            'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
            'Cookie': 'current_odin_platform=pc; SSO_AS_SUB_TICKET3114=24b0ae5cfb0b962c24382ad0d91821fe0003114000; SSO_AS_UID3114=elysianiu_i; odin_jwt_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NTAzMzM2NTcsImlhdCI6MTc0Nzc0MTY1NywiaXNzIjoib2Rpbi54aWFvanVrZWppLmNvbSIsInN1YiI6ImVseXNpYW5pdV9pIn0.BVH9Yc2lBP9WNquwFLUwVicsa0C3x6UtDda-x8JMNkI; _kylin_username=elysianiu_i; _kylin_username_zh=%E7%89%9B%E6%AD%86%E5%AA%9B; _OMGID=52c10386-731a-4c43-ab98-dbb017e433f8; _product_id=1; CASE_SSO_USERNAME=elysianiu_i; username=elysianiu_i; ENG_prod_SESSION_ID=b2a19231ff9932e74341ffe01da5501a000915000; _kylin_ticket=99ac7e2b3ca0b6cc54662f4ff69894940001268000; __hash__wa=20250605-didifarm-elysianiu_i-adf808f8-afe6-4e48-9b5a-343192470e66; __hash__cache=adf808f8-afe6-4e48-9b5a-343192470e66; user-fingerprint-water-mark=20250605-didifarm-elysianiu_i-adf808f8-afe6-4e48-9b5a-343192470e66'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        data = response.json()
        oid = data["data"]["oid"]
        return oid
