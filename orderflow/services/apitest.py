import requests
import json


class ApitestRequest(object):
    def debug_run(self, run_step_uuid, variables):
        '''获取 id 用于执行 case

            Args:
            run_step_uuid (str): case 的步骤 id
            variables (dict): case执行所需变量

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
            "variables": variables
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
        response = requests.request("POST", url, headers=headers, data=params)
        data = response.json()
        run_record = data["status"]
        return run_record
    
    