def newPrice(price, price_raise):
    return price + (price / 100 * price_raise)

goods_count = int(input('Введите количество товаров: '))
goods_prices = [float(input('Цена на товар: ')) for _ in range(goods_count)]

raise_firstyear = int(input('Повышение на первый год: '))
raise_secondyear = int(input('Повышение на второй год: '))

prices_firstyear = [newPrice(price, raise_firstyear) for price in goods_prices]
prices_secondyear = [newPrice(price, raise_secondyear) for price in goods_prices]

print('Суммы цен за каждый год:', round(sum(goods_prices), 2), round(sum(prices_firstyear), 2), round(sum(prices_secondyear), 2))
