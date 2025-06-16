import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from orders.fast import OrderFlowFast

@pytest.mark.parametrize("phone", ["00012017804"])
def test_end(phone):
    '''测试结束订单

            Args:
            phone (str): 您的线上乘客号码

            Returns:
            result: 执行结束订单

        '''
    hailing_client = OrderFlowFast()
    variables = hailing_client.create_order(phone)
    result = hailing_client.complete_order(variables)
    print(result)
