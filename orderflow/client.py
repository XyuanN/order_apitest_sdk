import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from orders.fast import OrderFlowFast


if __name__ == '__main__':
    phone = sys.stdin.readline().strip()
    hailing_client = OrderFlowFast()
    variables = hailing_client.create_order(phone)
    hailing_client.accept_order(variables)
    hailing_client.driver_arrived(variables)
    hailing_client.start_trip(variables)
    hailing_client.complete_order(variables)
