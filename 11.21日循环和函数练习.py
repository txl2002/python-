'''age=17
print(f"今年我已经{age}岁了")
if age>17:
    print("我已经成年了")
print("时间过的真快")
#if语句后记得加上：这个符号#



print("欢迎来到黑马儿童游乐场，儿童免费，成人收费")
age = int(input("请输入你的年龄"))
#input返回的是字符串，必须加int（）转换成整数类型#
if age >=18:
    print('您需要买票')
else :
    print("不需要买票")




print("欢迎来到黑马动物园")
age = int(input('请输入您的身高:'))
if age > 120:
    print("身高超出120，需要购票")
else:
    print("未超出120，不要买票")
'''
'''
import random
num = random.randint(1,10)
print("请猜一下这个数字是什么")
if int(input("第一次机会：")) == num:
    print("你猜对了")
else:
    print("nicaiduol")
'''
'''i = 0
sum = 0
while(i<101):
    sum += i
    i=i+1
print(sum)
'''

'''i = 1
while (i<=9):
    j=1
    while(i>=j):
        print(f"{j}*{i}={j * i}\t",end = " ")
        j += 1
    i += 1
    print()
'''
'''name = "itheima is a brand of itcast"
i = 0
for x in name:
    if x=='a':
        i +=1
print(i)
'''
'''i=0
for x in range(1,100):
    if x%2 ==0:
        i +=1
print(i)
'''
# i = 0
# for i in range(1, 101):
#     print(f"向txl表白的第{i}天")
#     for j in range(1, 11):                              ctrl加/  为多端注释
#         print(f"第{j}多玫瑰")
#     print(f"这是我喜欢你的第{i}天")
#
# print(f"第{i}天，表白成功")#这里若要引用i变量，但已经超出了for的作用域，所以需要在开头定义i变量



# sum_wage=10000
# import random
# for i in range(1,21):
#     score=random.randint(1,11)
#     if score<5:
#         print(f"员工{i}，绩效分{score}，不发工资，下一位")
#         continue
#     else:
#         sum_wage=sum_wage-1000
#         print(f"员工{i}，绩效{score},账户余额为{sum_wage}")
#         if(sum_wage==0):
#             print("工资发完了")
#             break


# def add(x, y):
#     result = x + y
#     print(f"结果是：{result}")
#
# add(5,7)

# def check(t):
#     if t < 37.5:
#         print("请进")
#     else:
#         print("需要隔离")
#
# check(36)


#函数返回值的应用
# def add(x, y):
#     result = x + y
#     return result           # return后写要返回的值   注意：函数体在遇到return后就结束了，写在return后的都不会去执行
# r = add(5,8)                #定义一个变量去接收这个result
# print(r)                    #最后再把这个值输出

# 函数定义的格式：  def 函数名字（参数）:
#                     函数体
#                     return 返回值
#                     变量 = 函数（参数）