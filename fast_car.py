import sys
from base import APITEST_FAST

class TakeOrder(object):
    def take_order(self, phone):
        query = APITEST_FAST(phone)
        debug_id, run_record_id = query.debug_run(run_step_uuid = "fcd42daa-a842-4635-a1c7-c6fd0f1a6388")
        result = query.debug_result(debug_id, run_record_id)
        return result
    
class DriverArrived(TakeOrder):
    def arrived(self, phone):
        self.take_order(phone)
        query = APITEST_FAST(phone)
        debug_id, run_record_id = query.debug_run(run_step_uuid = "95157916-d13a-43d5-89b8-c2a7c3d50383")
        result = query.debug_result(debug_id, run_record_id)
        return result
    
class BeginOrder(DriverArrived):
    def begin_charge(self, phone):
        self.arrived(phone)
        query = APITEST_FAST(phone)
        debug_id, run_record_id = query.debug_run(run_step_uuid = "1f5d7f1e-8cac-4b43-8fc7-82df8cc530b8")
        result = query.debug_result(debug_id, run_record_id)
        return result
    def end_charge(self, phone):
        query = APITEST_FAST(phone)
        debug_id, run_record_id = query.debug_run(run_step_uuid = "112d3d4c-6306-4bff-bb15-f1d3b5dc5231")
        query.debug_result(debug_id, run_record_id)
        return 
    
class EndOrder(BeginOrder):
    def end(self, phone):
        self.begin_charge(phone)
        self.end_charge(phone)
        query = APITEST_FAST(phone)
        debug_id, run_record_id = query.debug_run(run_step_uuid = "10e49ed4-37b4-487e-a49c-0d444e4940c4")
        result = query.debug_result(debug_id, run_record_id)
        return result

if __name__ == '__main__':
    number = sys.stdin.readline().strip()
    # jiedan = TakeOrder()
    # result = jiedan.take_order(number)
    # daoda = DriverArrived()
    # result = daoda.arrived(number)
    # kaishi = BeginOrder()
    # result = kaishi.begin_charge(number)
    jieshu = EndOrder()
    result = jieshu.end(number)
    print(result)