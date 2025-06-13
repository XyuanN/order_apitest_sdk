import pytest 
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from mypackage.modules.order import OrderFast

@pytest.mark.parametrize("phone", ["00012017804"])
def test_end(phone):
    '''测试结束订单

            Args:
            phone (str): 您的线上乘客号码

            Returns:
            result: 执行结束订单

        '''
    result = OrderFast(phone).end()
    print(result)
