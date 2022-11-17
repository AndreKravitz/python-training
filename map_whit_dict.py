# Original list
items = [
    {
        'product': 'shirt',
        'price': 30,
    },
    {
        'product': 'pant',
        'price': 70
    },
    {
        'product': 'sneakers',
        'price': 100
    }
]

# Creating new item (taxes)


def add_taxes(item):
    new_item = item.copy()
    new_item['taxes'] = new_item['price'] * 2.9
    return new_item


# New list with taxes
taxed_items = list(map(add_taxes, items))

print('New list whit taxes')
print(taxed_items)
print('Original list')
print(items)
