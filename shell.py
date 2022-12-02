from shop.models import Item, Purchase

item = Item.objects.create(name='iPhone 13 Pro', price=1200)
item1 = Item.objects.create(name='Asus Rog laptop', price=980)
item2 = Item.objects.create(name='Samsung Fridge', price=300)
item3 = Item.objects.create(name='Samsung Phone', price=600)
item4 = Item.objects.create(name='Xiaomi Phone', price=580)
item5 = Item.objects.create(name='AirPods pro', price=229)
item6 = Item.objects.create(name='Samsung Earpods', price=114)
item7 = Item.objects.create(name='Samsung TV', price=870)
item8 = Item.objects.create(name='MacBook Air', price=1500)
item9 = Item.objects.create(name='Steelseries mouse', price=85)

item.purchases.create(name='Iman', age=19)
item.purchases.create(name='Akim', age=43)
item1.purchases.create(name='Akim', age=25)
item1.purchases.create(name='Tima', age=25)
item2.purchases.create(name='Tima ', age=25)
item2.purchases.create(name='Danil ', age=25)
item3.purchases.create(name='Iman ', age=25)
item3.purchases.create(name='Aiym ', age=25)
item4.purchases.create(name='Aiym ', age=25)
item4.purchases.create(name='Tima ', age=25)
item5.purchases.create(name='Chika ', age=25)
item5.purchases.create(name='Iman', age=25)
item6.purchases.create(name='Arina', age=25)
item6.purchases.create(name='Bek', age=25)
item7.purchases.create(name='Rustam', age=25)
item7.purchases.create(name='Uluk', age=25)
item8.purchases.create(name='Edil', age=25)
item8.purchases.create(name='Nursultan', age=25)
item9.purchases.create(name='Iman', age=25)
item9.purchases.create(name='Bek', age=25)



item.choices.all()


