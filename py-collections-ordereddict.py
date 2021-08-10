from collections import OrderedDict

items = int(input())

shop_items = OrderedDict()
for i in range(items):
    item = input().split()
    price = int(item.pop())
    item_name = ' '.join(item)
    shop_items[item_name] = shop_items.get(item_name, 0) + price

for item_name, net_price in shop_items.items():
    print(item_name, net_price)
