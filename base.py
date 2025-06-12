import requests
import json

uuid_list = {
    "司机接单": "fcd42daa-a842-4635-a1c7-c6fd0f1a6388", #司机接单
    "司机到达": "95157916-d13a-43d5-89b8-c2a7c3d50383", #司机到达
    "开始计费": "1f5d7f1e-8cac-4b43-8fc7-82df8cc530b8", #开始计费
    "结束计费": "112d3d4c-6306-4bff-bb15-f1d3b5dc5231", #结束计费
    "结束订单": "fb7dabb0-60f8-4402-b8e0-b2bf9a439ad2" #结束订单
    }

class GetOid(object):
    def get_pid(self, phone):
        '''获取乘客账号的pid

            Args:
            phone (str): 线上乘客手机号

            Returns:
            pid: 手机号pid

        '''
        url = "https://didifarm.intra.xiaojukeji.com/beta/api/didifarm/v1/data/PhoneToUid/?dev=1&role=1&countryCode=86&phone="+str(phone)
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
        response = requests.request("GET", url, headers = headers, json = payload)
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
        response = requests.request("POST", url, headers = headers, data = payload)
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
        response = requests.request("POST", url, headers = headers, data = payload)
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
        response = requests.request("POST", url, headers = headers, data = payload)
        data = response.json()
        oid = data["data"]["oid"]
        return oid

class APITEST_FAST(GetOid):
    def __init__(self, phone):
        super().__init__()
        self.pid = self.get_pid(phone)
        self.low_oid = self.get_low_oid(self.pid)
        self.high_oid = self.get_high_oid(self.low_oid)
        self.oid = self.get_oid(self.low_oid)

    def debug_run(self, run_step_uuid):
        '''获取 id 用于执行 case

            Args:
            run_step_uuid (str): case 的步骤 id

            Returns:
            debug_id: 执行 case 所需参数
            run_record_id: 执行 case 所需参数

        '''
        url = "http://api.eng.xiaojukeji.com/api/open/apitest/debug-run"
        params = json.dumps({
            "case_id": 486241,
            "env_name":"线上环境",
            "run_step_uuids":[
                run_step_uuid
            ],
            "variables":[
                {
                    "name":"highOid",
                    "value": self.high_oid

                },
                {
                    "name":"oid",  
                    "value":self.oid
                },
                {
                    "name":"group_key",  
                    "value":"3_600_0"
                },
                {
                    "name":"require_level",  
                    "value":"600"
                },
                {
                    "name":"product_id",  
                    "value":"3"
                },
                {
                    "name":"cityid",  
                    "value":"1"
                },
                {
                    "name":"combo_type",  
                    "value":"0"
                }
            ]
        })
        headers = {
            'token': '3911AD9B440D9BBFA0B7D17EC76BFA3C',
            
        }
        response = requests.request("POST", url, headers=headers, data=params)
        data = response.json()
        debug_id = data['data']['debug_id']
        run_record_id = data['data']['run_record_id']
        return debug_id, run_record_id
    
    def debug_result(self, debug_id, run_record_id):
        ''' case执行

            Args:
            debug_id: 由 debug_run 获得
            run_record_id: 由 debug_run 获得

            Returns:
            run_record: 步骤执行状态

        '''
        url = "http://api.eng.xiaojukeji.com/api/open/apitest/debug-result"
        params = json.dumps({
            "debug_id": debug_id,
            "run_record_id": run_record_id
        })
        headers = {
            'token': '3911AD9B440D9BBFA0B7D17EC76BFA3C'
        }
        response = requests.request("POST", url, headers = headers, data = params)
        data = response.json()
        run_record = data["status"]
        return run_record
    
    