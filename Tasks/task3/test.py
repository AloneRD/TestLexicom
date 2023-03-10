import sys
import os

sys.path.append(os.path.join('...','..'))


from Tasks.task1.test import ServiceCenter
from Tasks.task2.test import get_file_name


service_center = ServiceCenter()
orders = service_center.get_orders()

for order in orders:
    print(order)

print(get_file_name(['ertffdfe','re','erffdsrttdg']))

