#实现输入10个数字，并打印10个数的求和结果
# start = 1
# s = []
# while start <= 10:
#     num = input("请输入数字")
#     num = int(num)
#     s.append(num)
#     start = start + 1
#     #总和
# print(sum(s))
#     #平均数
# print(sum(s)/10)
#     #最大数
# print(max(s))
#     #最小数
# print(min(s))

#从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数。
# start = 1
# s = []
# while start <= 10:
#     num = input("请输入数字")
#     num = int(num)
#     s.append(num)
#     start = start + 1
#     #总和
#     print(sum(s))
#     #平均数
#     print(sum(s)/10)

# '''
# 从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形（结果判断：等腰，等边，直角，普通，不能形成三角形。）
# '''
# a = input("请输入三角形第一个边")
# b = input("请输入三角形的第二个边")
# c = input("请输入三角形的第三个边")
# a=int(a)
# b=int(b)
# c=int(c)
#
# if a == b and b == c:
#     print("等边三角形")
# elif a == b:
#     print("等腰三角形")
# elif(a*b) == (c*c):
#     print("直角三角形")
# else:
#     print("普通三角形")
#

for i in range(7):
    print(" " * (8 - i), end="")
    print(" * " * (i + 1))
