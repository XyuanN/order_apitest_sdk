import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.apitest import ApitestRequest


#apitest请求为父类，订单流转为其中的一个子类
class OrderFlow(ApitestRequest):
    def __init__(self):
        self.uuid_1 = ""
        self.uuid_2 = ""
        self.uuid_3 = ""
        self.uuid_4 = ""
        self.uuid_5 = ""

    def accept_order(self, variables):
        debug_id, run_record_id = ApitestRequest().debug_run(self.uuid_1, variables)
        result = ApitestRequest().debug_result(debug_id, run_record_id)
        return result
    
    def driver_arrived(self, variables):
        self.accept_order(variables)
        debug_id, run_record_id = ApitestRequest().debug_run(self.uuid_2, variables)
        result = ApitestRequest().debug_result(debug_id, run_record_id)
        return result
    
    def start_trip(self, variables):
        self.driver_arrived(variables)
        debug_id, run_record_id = ApitestRequest().debug_run(self.uuid_3, variables)
        result = ApitestRequest().debug_result(debug_id, run_record_id)
        return result
    
    def end_charge(self, variables):
        debug_id, run_record_id = ApitestRequest().debug_run(self.uuid_4, variables)
        ApitestRequest().debug_result(debug_id, run_record_id)
        return 
    
    def complete_order(self, variables):
        self.start_trip(variables)
        self.end_charge(variables)
        debug_id, run_record_id = ApitestRequest().debug_run(self.uuid_5, variables)
        result = ApitestRequest().debug_result(debug_id, run_record_id)
        return result