from teaching.data import Drink

balance = 0
drinks = {
    Drink(),
    {'name': '可樂', 'price': 20},
    {'name': '雪碧', 'price': 25},
    {'name': '茶裏王', 'price': 20},
    {'name': '原萃', 'price': 30},
    {'name': '純粹喝', 'price': 25},
    {'name': '水', 'price': 15},
}
def deposit():
    global balance #代表呼叫外面的balance 函式裡面用的變數跟外面用的不一樣
    value = eval(input('儲值金額:'))
    while value < 1:
        print('====儲值金額需大於0====')
        value = eval(input('儲值金額:'))
    balance += value
    print(f'儲值後餘額為{balance}元')
def buy():
    global balance
    print('請選擇商品')
    for i in range(0, len(drinks)):
        print(f'({i + 1}) {drinks[i].name} {drinks[i].price}元')
    choose = eval(input('請選擇:'))
    while choose < 1 | choose > 6:
        print('請輸入1~6之間')
        choose = eval(input("請選擇:"))
    buy_drink = drinks[choose - 1]
    while balance < buy_drink.price:
        print('餘額不足要儲值嗎?')
        want_deposit = input('y/n?')
        if want_deposit=='y':
            deposit()
        elif want_deposit == 'n':
            break
        else:
            print('請重新輸入')
    if (balance < buy_drink.price):
        print('餘額不足')
        deposit()
    else:
        balance -= buy_drink.price
        print(f'已購買{buy_drink.name}')
        print(f'{buy_drink.name} {buy_drink.price}:元')
