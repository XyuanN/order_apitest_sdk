import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.oid import OrderOid
from orders.base import OrderFlow


class OrderFlowFast(OrderFlow):
    def __init__(self):
        super(OrderFlow, self).__init__()
        self.uuid_1 = "fcd42daa-a842-4635-a1c7-c6fd0f1a6388"
        self.uuid_2 = "95157916-d13a-43d5-89b8-c2a7c3d50383"
        self.uuid_3 = "1f5d7f1e-8cac-4b43-8fc7-82df8cc530b8"
        self.uuid_4 = "112d3d4c-6306-4bff-bb15-f1d3b5dc5231"
        self.uuid_5 = "10e49ed4-37b4-487e-a49c-0d444e4940c4"

    def create_order(self, phone):
        self._pid = OrderOid(phone).get_pid()
        self._low_oid = OrderOid(phone).get_low_oid(self._pid)
        self._high_oid = OrderOid(phone).get_high_oid(self._low_oid)
        self._oid = OrderOid(phone).get_oid(self._low_oid)
        
        variables = [
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
        return variables