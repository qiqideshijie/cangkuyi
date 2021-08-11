import copy
import random

b = 1  # 机械革命
c = 1  # HUA WEI WATCH
d = 1  # 卫龙辣条

shop = [
    ["lenovo PC", 5600],
    ["HUA WEI WATCH", 1200],
    ["Mac pro", 12000],
    ["洗衣机", 3000],
    ["机械革命", 5000],
    ["卫龙辣条", 4.5],
    ["老干妈辣酱", 20],
]

a = random.randint(0, 44)

# 1.准备好钱包

money = input("欢迎来到我的supermaker")
money = int(money)
ticket = input("您要参与抽奖吗？\n yes/no(y/s)?\n")
if ticket == "y":

    if a >= 0 and a <= 9:
        b = 0.5
        shop[4][1] = round(shop[4][1] * b, 2)

        print("机械革命五折优惠券")
    elif a > 9 and a <= 29:
        d = 0.3
        shop[5][1] = round(shop[5][1] * d, 2)
        print("卫龙辣条三折优惠券")
    elif a > 29 and a <= 44:
        c = 0.8
        shop[1][1] = round(shop[1][1] * c, 2)
        print("HUA WEI WATCH八折优惠券")
else:
    pass

# 2. 准备一个空的购物车
mycart = []

sum = 0
# 3.开始购物
sum = 0
i = 0
while i < 20:
    for key, value in enumerate(shop):
        print(key, value)
        # 请输入您要卖的商品
    chose = input("请输入您要买的商品:")

    if chose.isdigit():
        chose = int(chose)  # "1" --> 1
        if chose > len(shop) or chose < 0:  # 9 > 7
            print("抱歉，由于个人原因商品暂未上架")
        else:
            if money >= shop[chose][1]:
                money = money - shop[chose][1]
                mycart.append(copy.deepcopy(shop[chose]))
                sum = sum + shop[chose][1]
                print("您已经把您的商品添加到了购物车！您的余额为：￥", money)
                if b != 1 and chose == 4:
                    shop[4][1] = 5000
                elif c != 1 and chose == 1:
                    shop[1][1] = 1200
                elif d != 1 and chose == 5:
                    shop[5][1] = 4.5
    elif chose == "q" or chose == "Q":
        print("欢迎下次光临！")
        break

print("以下是您的购物小条!!!")
print("".center(30,"-"))
for key,value in enumerate(mycart):
    print(key,value)
print("".center(30,"-"))