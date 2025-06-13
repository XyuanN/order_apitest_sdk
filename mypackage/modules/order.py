import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tools.execute import ApitestFast


class OrderFast(object):
    def __init__(self, phone):
        self.phone = phone
        self.uuid_1 = "fcd42daa-a842-4635-a1c7-c6fd0f1a6388"
        self.uuid_2 = "95157916-d13a-43d5-89b8-c2a7c3d50383"
        self.uuid_3 = "1f5d7f1e-8cac-4b43-8fc7-82df8cc530b8"
        self.uuid_4 = "112d3d4c-6306-4bff-bb15-f1d3b5dc5231"
        self.uuid_5 = "10e49ed4-37b4-487e-a49c-0d444e4940c4"

    def take_order(self):
        debug_id, run_record_id = ApitestFast(self.phone).debug_run(self.uuid_1)
        result = ApitestFast(self.phone).debug_result(debug_id, run_record_id)
        return result
    
    def arrived(self):
        self.take_order()
        debug_id, run_record_id = ApitestFast(self.phone).debug_run(self.uuid_2)
        result = ApitestFast(self.phone).debug_result(debug_id, run_record_id)
        return result
    
    def begin_charge(self):
        self.arrived()
        debug_id, run_record_id = ApitestFast(self.phone).debug_run(self.uuid_3)
        result = ApitestFast(self.phone).debug_result(debug_id, run_record_id)
        return result
    
    def end_charge(self):
        debug_id, run_record_id = ApitestFast(self.phone).debug_run(self.uuid_4)
        ApitestFast(self.phone).debug_result(debug_id, run_record_id)
        return 
    
    def end(self):
        self.begin_charge()
        self.end_charge()
        debug_id, run_record_id = ApitestFast(self.phone).debug_run(self.uuid_5)
        result = ApitestFast(self.phone).debug_result(debug_id, run_record_id)
        return result