这是一个快车线上环境进行订单流转的sdk，能够实现司机接单，司机到达，开始计费，结束订单

## 安装依赖
```
python3 install -r requirements.txt
```
## 导入库
```
from order import fast
from fast import TakeOrder, DriverArrived, BeginOrder, EndOrder
```
## 订单流转
```
TakeOrder.take_order(passenger_number)
DriverArrived.arrived(passenger_number)
BeginOrder.begin_charge(passenger_number)
EndOrder.end(passenger_number)
```