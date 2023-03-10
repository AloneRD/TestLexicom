from typing import Iterable


class ServiceCenter:
    __db = {
        ('Татьяна', '890002001020'): [('Ноутбук',1200), ('Ноутбук', 4800)],
        ('Сергей', '89808564559'): [('Сканер', 550)]
    }
    
    def get_orders(self) -> Iterable[str]:
        for client_name, orders in self.__db.items():
            yield f'{" ".join(client_name)} : {orders}'
    
    def add_order(self, client_name: str, number_phone:str, technic_name: str, price:str) -> str:
        if (client_name, number_phone) not in self.__db:
            self.__db[(client_name, number_phone)] = [(technic_name, price)]
        else:
            self.__db[(client_name, number_phone)].append((technic_name, price))
        
        return 'Заказ добавлен'
