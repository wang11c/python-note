#!/usr/bin/env python
# coding: utf-8

# 课时5
# 
# 转义字符
# 如果真的要用\，如c:\user，就打两个

# In[1]:


s="c:\user"
print(s)


# In[30]:


s="c:\\user"
print(s)


# 如果打印ss='let's go'

# In[31]:


ss='let's go'
print(ss)


# In[33]:


ss='let\'s go'
print(ss)


# \要放在'的前面才能转义

# In[38]:


s1= "i love \n jb"
print(s1)


# \n表示换行

# 如果想要字符串格式化，把字符串按照一定格式打印或者填充
# 如：
# s="XXX,不吃白不吃，吃了也白吃" XXX用人名填充
# 1.用百分号 %d代表整数， %s代表一个字符串
# 2.用format函数

# In[41]:


s="%s,i love you" %"王川"
print(s)


# In[45]:


s= "i am %d years old" %18
print(s)


# In[49]:


s= "i am %d years old"
print(s%18)


# 一句话里有几个占位符，就必须要有几个占位符代替

# In[59]:


s= "i am %s, i am %d years old" 
print(s%("王川",18))


# 推荐使用format函数，以｛｝和：代替%号

# In[62]:


s="i love {}".format("王川")
print(s)


# In[64]:


s="i am {1} years old, i love {0} and i am {1} years old.".format("王川",18)
print(s)


# 算数运算符，乘号用*，除号用/

# In[68]:


a=5+2
b=5*2
c=5/2
print(a)
print(b)
print(c)


# python 2.0和python3.0，除号结果可能不一致
# 
# % 取余数运算

# In[70]:


a=9%4
print(a)


# //表示取商运算，也叫地板除

# In[72]:


a=9//4
print(a)


# **表示幂运算

# In[1]:


a=9**2
print(a)


# 比较运算符：对两个变量或者值进行比较，比较的结果是个布尔值true/false

# In[4]:


b=a==80
b


# 81等于80，所以False

# !=不等于 >=大于等于 <=小于等于

# 赋值运算符 

# In[5]:


#=
a=0
c=a=4
#缩写 += a+=7就是a=a+7 还有-= /= //= **=


# 逻辑运算符 对布尔值进行计算的符号
# and 逻辑与  or 逻辑或  not 逻辑非 
# 运算规则：and看做乘法，or看做加法，true看做1，false看做2
# 最后结果如果是0则为false，否则为true

# In[11]:


a=True
b=False
c=True
d=a and b or c  #a*b+c
print(d)
e= a or b and a #1+0*1
print(e)


# 逻辑运算的短路问题：逻辑运算式，按照顺序计算，一旦能够确定整个式子未来的值，则不再进行计算，直接返回

# In[13]:


#短路示例
a= True or xxxxxxxx
#运行到or的时候，整个表达式不再向下计算
print(a)


# 成员运算符号 用来检测某一个变量是否是另外一个变量的成员
# in, not in

# In[ ]:


l=[1,2,3,4,5]
a=7
b=a in l
print(b)
e=4
print(e not in l)


# 身份运算 
# is 用来检测两个变量是否是同一个变量 语法就是var1 is var2
# is not 两个变量不是同一个变量

# In[ ]:


a=9
b=9
print(a is b)


# 运算符的优先级问题
# -永远记住，括号具有最高优先级
# **指数 最高优先级

# 三大结构
# -顺序
# -分支
# -循环
# 
# 分支
# -分支的基本语法
# if条件表达式：
# 语句1
# 语句2
# 语句3
# ......
# 
# 条件表达式就是计算结果必须为布尔值的表达式，结果为true执行后面的语句块
# 表达式后面的冒号不能少
# 如果if后面出现的语句属于一个语句块，则必须在同一缩进等级

# In[25]:


age=19
if age<18:
    print("去叫家长吧，孩纸")
    print("我们不带你玩儿")
    
print("老司机")
# 前两句print是在if里，第三句是单独的


# #双向分支
# if...else...语句
# if 条件表达式：
#    语句1
#    语句2
#    ...
# else：
#    语句1
#    语句2
#    ...

# In[ ]:


gender=input("输入性别：")
print("你输入的性别是:{0}".format(gender))
if gender=="nan":
    print("来吧")
else:
    print("别来了")


# In[ ]:


score=input("请输入学生成绩：")
#字符串不能和数字直接比较，字符串要转换成数字
score=int(score)
if score>=90:
    print("A")
if score >=80 and score<90:
    print("B")
if score >=70 and score<80:
    print("C")
if score >=60 and score<70:
    print("D")


# 多路分支  可以替换上面
# -很多分支的情况
# 
# if 条件表达式：
#     语句1
#     ...
# elif 条件表达式：
#     语句1
#     ...
# 
# else:
#     语句1
#     ...
# 
# -elif可以有无数个
# -else可以没有
# -多路分支只会选一个执行

# In[ ]:


score=input("请输入学生成绩：")
score=int(score)
if score>=90:
    print("A")
elif score >=80 and score<90:
    print("B")
elif score >=70 and score<80:
    print("C")
elif score >=60 and score<70:
    print("D")
else
    print("你不是我学生")


# if语句其他：
# -if语句可以嵌套使用，但是不推荐

# 循环语句
# -重复执行某些固定动作或者处理基本固定的事物
# -分类
#     - for循环
#     - while循环
# for循环
# 
#     for 变量 in 序列：
#         语句1
#         语句2
#         ...

# In[ ]:


#列表就是一列数字或者其他值，一般用中括号表示
#例如 ["yi"，"er"，"san"]
#打印列表
for name in  ["yi"，"er"，"san"]：
    print("name")
    if name = "yi"：
        print("是我的{0}.format(name)")
    else:
        print("不是我")


# range介绍
# -生成一个数字序列
# -具体范围可以设定
# -数字范围包左不包右
# -range函数在python2和python3中区别很大

# In[ ]:


for i in range(1,10)：
    print(i)


# for-else语句
# -当for循环结束的时候，执行else语句
# -else语句是可选语句

# In[13]:


#打印的东西不在列表中，需要有提示语句
for name in  ["yi","er","san"]:
    print("name")
    if name == "yi":
        print("是我的{0}.format(name)")
    else:
        print("不是我")
else:
    print("不在")


# In[ ]:


##循环之break, countinue, pass
-break:一旦执行到这，无条件结束整个循环，简称循环猝死
-continue：无条件结束本次循环，重新进入下一轮循环
-pass:表示略过，一般用于占位


# In[5]:


#在1-10的数字中寻找数字7，一旦找到了，就打印出来，其他什么都不做
for i in range(1,11):
    if i==7:
        print("找到了")
        break
    else:
        print(i)


# In[ ]:


#在1-10的数字中寻找所有偶数，一旦找到了，就打印出来
for i in range(1,11):
    if i%2==1：#基数
        continue
    else:
        print("{0}是偶数.format(i)")


# In[3]:


for i in range(1,11):
    pass
    print("一二三")

