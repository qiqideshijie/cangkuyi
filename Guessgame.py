import random

user = input ("请输入 用户名")
if user == "admin":
    passwd = input ("请输入密码")
    if passwd == "root":
         print ("登录成功，您目前有500金币")
    else:
        print ("密码输入错误")
else:
    print ("用户名输入有误，请重新输入")
money = 500
num = random.randint(0, 100)
count = 1
j = 50
while money >= 50:
    c = j * count
    ym = money - c
    count = count + 1
    chose = input("请输入您要的猜的数字：")
    chose = int(chose)
    if chose > num:
        print("大了，您现在还剩", ym, "现在是第", count, "几步")
        if money < 50:
            print("金币数量不足，游戏结束")
            break
    elif chose < num:
        print("小了，您现在还剩", ym, "现在是第", count, "几步")
        if money < 50:
            print("金币数量不足，游戏结束")
            break
    else:
        print("恭喜，您猜中了，本次数字为：", num, "，您本次输入了", count, "次！", "还剩", ym, "金币")
        money = money + 500
        n=input("继续？（y/n）")
        if n=="y":
            continue
        elif n=="n":
            break
        else:
            print("输入有问题")
            break