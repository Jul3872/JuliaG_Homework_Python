from smartphone import Smartphone

catalog = [Smartphone('Apple', 'iPhone 14 Pro Max', '+79998887766'),
           Smartphone('Samsung', 'Galaxy S23 Ultra', '+79997776655'),
           Smartphone('Xiaomi', 'Redmi Note 11S', '+79996665544'),
           Smartphone('Huawei', 'P50 Pro', '+79995554433'),
           Smartphone('OnePlus', '9T', '+79994443322')
           ]
for phone in catalog:
    print(f'{phone.brand} - {phone.model}.'
          f'{phone.phon_num}')
