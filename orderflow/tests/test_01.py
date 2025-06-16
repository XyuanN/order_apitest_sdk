import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from orders.fast import OrderFlowFast


@pytest.mark.parametrize("phone", ["00012019829"])
def test_takeorder(phone):
    '''测试司机接单

            Args:
            phone (str): 您的线上乘客号码

            Returns:
            result: 执行司机接单

        '''
    hailing_client = OrderFlowFast()
    variables = hailing_client.create_order(phone)
    result = hailing_client.accept_order(variables)
    print(result)