# 🌟 Order APITest SDK
Order APITest SDK 是一个实现线上环境快车订单流转的 sdk，通过导入 sdk，你能够实现端到端的司机接单，司机到达，开始计费，结束订单的 UI 自动化。

## 🚀 快速开始

1. **克隆仓库** 

    ```bash 
    git clone git@git.xiaojukeji.com:dmq/order_apitest_sdk.git
    ```

2. **安装依赖**

    ```bash
    pip install -r requirements.txt
    ```

2. **调用**

    ```bash
    from orderflow import OrderFlowFast
    
    # 创建订单
    hailing_client = OrderFlowFast()
    variables = hailing_client.create_order(phone)
    
    # 订单流转
    hailing_client.accept_order(variables)
    hailing_client.driver_arrived(variables)
    hailing_client.start_trip(variables)
    hailing_client.complete_order(variables)
    ```

## 🧐 即将上线
后续 Order APITest SDK 会新增专车、豪车等不同车型的订单流转功能。