import requests
import json
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tools.oid import OrderOid


class ApitestFast(object):
    def __init__(self, phone):
        self._pid = OrderOid(phone).get_pid()
        self._low_oid = OrderOid(phone).get_low_oid(self._pid)
        self._high_oid = OrderOid(phone).get_high_oid(self._low_oid)
        self._oid = OrderOid(phone).get_oid(self._low_oid)

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
                    "value": self._high_oid

                },
                {
                    "name":"oid",  
                    "value":self._oid
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
    
    