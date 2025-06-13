import pytest 
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from mypackage.modules.order import OrderFast

@pytest.mark.parametrize("phone", ["00012017804"])
def test_begin(phone):
    '''测试开始计费

            Args:
            phone (str): 您的线上乘客号码

            Returns:
            result: 执行开始计费

        '''
    result = OrderFast(phone).begin_charge()
    print(result)
