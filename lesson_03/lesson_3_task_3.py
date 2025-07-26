from address import Address
from mailing import Mailing

from_addr = Address(index='123456', city='Москва',
                    street='Ленинградская', house='10', apartment='56')

to_addr = Address(index='123789', city='Химки', street='Дружбы',
                  house='78', apartment='3')

mailing = Mailing(to_address=to_addr, from_address=from_addr,
                  cost=500, track='TRACK123')

print(f'Отправление {mailing.track} '
      f'из {mailing.from_address.index}, {mailing.from_address.city}, '
      f'{mailing.from_address.street}, {mailing.from_address.house} - '
      f'{mailing.from_address.apartment} '
      f'в {mailing.to_address.index}, {mailing.to_address.city}, '
      f'{mailing.to_address.street}, {mailing.to_address.house} - '
      f'{mailing.to_address.apartment}. '
      f'Стоимость {mailing.cost} рублей.')
