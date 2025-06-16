import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from orders.fast import OrderFlowFast

@pytest.mark.parametrize("phone", ["00012017804"])
def test_arrived(phone):
    '''测试司机到达

            Args:
            phone (str): 您的线上乘客号码

            Returns:
            result: 执行司机到达

        '''
    hailing_client = OrderFlowFast()
    variables = hailing_client.create_order(phone)
    result = hailing_client.driver_arrived(variables)
    print(result)
