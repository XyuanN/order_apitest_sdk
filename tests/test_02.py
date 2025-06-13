import pytest 
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from mypackage.modules.order import OrderFast


@pytest.mark.parametrize("phone", ["00012017804"])
def test_arrived(phone):
    '''测试司机到达

            Args:
            phone (str): 您的线上乘客号码

            Returns:
            result: 执行司机到达

        '''
    result = OrderFast(phone).arrived()
    print(result)
