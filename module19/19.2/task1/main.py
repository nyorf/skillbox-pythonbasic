from urllib import request


small_storage = {
    'гвозди': 5000,
    'шурупы': 3040,
    'саморезы': 2000
}

big_storage = {
    'доски': 1000,
    'балки': 150,
    'рейки': 600
}

big_storage.update(small_storage)

search_request = input('Введите название товара: ').lower()
if big_storage.get(search_request) != None:
    print('Количество товара "{item}" на складе: {quantity}'.format(
        item = search_request,
        quantity = big_storage.get(search_request)
    ))
else:
    print('Товар "{item}" на складе отсутсвует.'.format(item = search_request))
