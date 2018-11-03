#!/usr/bin/env python
# coding: utf-8

# #while循环
# -一个循环语句
# -表示当某条件成立的时候，就循环
# -具体循环次数不知道，但能确定循环的成立条件的时候用while循环
# -while语法：
#     while 条件表达式：
#         语句块

# In[6]:


#年利率是6.7%，本钱多少年后翻倍
benqian = 10000
year = 0
while benqian < 20000:
    benqian=benqian*(1+0.067)
    year=year+1 #year+=1
    print("第{0}年拿了{1}块钱".format(year,benqian))


# 另一种表达方式：
#     while 条件表达式：
#         语句块1
#     else:
#         语句块2
#         

# In[8]:


benqian = 10000
year = 0
while benqian < 20000:
    benqian=benqian*(1+0.067)
    year=year+1 #year+=1
    print("第{0}年拿了{1}块钱".format(year,benqian))
else:
    print("终于翻倍了")


# 函数
# -代码的一种组织形式
# -函数使用需要先定义
# -使用函数，俗称调用
# #定义一个函数
# #只定义的话不会执行
# def func():
#     print("我是函数")
# #函数的调用 
# func()
# 直接函数名后面跟括号

# In[11]:


def func():
    print("我是函数")
func()


# -参数：负责给函数传递一些必要的数据或者信息
# 形式参数：在函数定义的时候用道德参数没有具体值，只是一个占位符号
# 实际参数：在调用函数的时候输入的值
# -返回值：函数的执行结果

# In[1]:


def hello(person):
    print("{0}，你好啊。".format(person))
    print("sir")
hello ("chuan")


# In[4]:


#return语句，函数完后返回的一句话，一旦执行完，无条件返回，不管后面的
def hi(person):
    print("我跟{0}打招呼，{1}没理我".format(person,person))
    
    return "不理我我走了"

hi("chuan")


# In[6]:


def hallo(person):
    print("我跟{0}打招呼，{1}没理我".format(person,person))
    
    return "不理我我走了"
    print("走人了")

hallo("chuan")


# In[11]:


#查找函数帮助文档，用help函数
help(print)


# 参数分类
# -普通参数
# -默认参数
# -关键字参数
# -收集参数
# 
# 普通参数
# -定义的时候直接定义变量名
# -调用的时候直接把变量或者值放入指定位置
# 
#     def 函数名(参数1，参数2,...)：
#         函数体
#         
#     调用
#     函数名(value1, value2,...):
#     
#     调用的时候，具体值参考的是位置，按位置赋值
# 
# 默认参数
# -形参带有默认值
# -调用的时候，如果没有相对应的参赋值，则使用默认值
# 
#     def func_name(pv=v1,pv=v2,...):
#         func_block
#         
#     调用1
#     func_name()  
#     用参数默认值
#     
#     调用2
#     value1=100
#     value2=200
#     func-name(value1,value2)
#     自己赋值

# In[19]:


#默认参数示例：(默认男生)
def reg(name, age, gender="male"):
    if gender =="male":
        print("{0} is {1} years old, and he is a good student.".format(name,age))
    else:
        print("{0} is {1} years old, and she is a good student.".format(name,age))
reg("史伯爵",18)    
reg("史伯爵",18,"female")   


# 关键字参数
# 语法
#     def func(p1=v1,p2=v2,...):
#         func_body
#        
#     调用函数：
#     func(p1=value1,p2=value2,...)
# 
# 比较麻烦，但也有好处：
# -不容易混淆，一般实参和形参只是按照位置一一对应即可，容易出错
# -关键字参数，可以不考虑参数位置

# In[22]:


def stu(name,age,addr):
    print("I am a student")
    print("我叫{0},我今年{1}岁了,我住{2}".format(name,age,addr))

n= "chuan"
a=18
addr="西单"
stu(n,a,addr)
#普通参数   


# In[4]:


#关键字参数
def stu_key(name="no name",age=0,addr="no addr"):
    print("I am a student")
    print("我叫{0},我今年{1}岁了,我住{2}".format(name,age,addr))

n= "chuan"
a=18
addr="西单"
stu_key(name=n,age=a,addr=addr)


# #收集参数
# -把没有位置，不能和定义时的参数位置相对应的参数，放入一个特定的数据结构中
# -语法
# 
#     def func(*args):
#         func_body
#         
#     调用：
#     func(p1,p2,p3,...)
# -参数名args不是必须这么写，但是推荐直接用args，约定俗成
# -参数名args前需要加星号*
# -收集参数可以和其他参数并存
# -把args看成一个列表List

# In[7]:


#函数模拟一个学生进行自我介绍，但具体内容不清楚
def stu(*args):
    print("hello,大家好，我自我介绍下：")
    #type函数作用是检测变量的类型
    print(type(args))
    for item in args:
        print(item)

stu("chuan",18,"北京","single")
stu("王先森")


# In[9]:


#收集参数案例
#说明收集参数可以不带任何实参调用，此时收集参数为空tuple
stu()


# 收集参数之关键字收集参数
# -把关键字参数按字典格式存入收集参数
#     def func(**kwargs):
#         func_body
#     
#     调用
#     func(p1=v1,p2=v2,...)
#     
# -kwargs一般约定俗成
# -调用的时候，把多余的关键字参数放入kwargs
# -访问kwargs需要按字典格式访问

# In[18]:


def stu(**kwargs):
    print("hello,自我介绍下")
    print(type(kwargs))
    for k,v in kwargs.items(): #key --- value
        print(k,"---",v)

stu(name="chuan",age=18,addr="北京西城",work="porn")
print("*******************")
stu(name="chuan")


# In[20]:


#收集参数为空的案例
stu()


# 收集参数混合调用的顺序问题
# -收集参数，关键字参数，普通参数可以混合使用
# -使用规则就是，普通参数和关键字参数优先
# -定义的时候一般找普通参数，关键字参数，收集参数tuple，收集参数dict

# In[40]:


#收集参数混合调用案例
#模拟学生自我介绍
def stu(name,age,hobby="没有",*args,**kwargs):
    print("hello,大家好")
    print("我叫{0},我今年{1}岁了。".format(name,age))
    if hobby=="没有":
        print("我没有爱好")
    else:
        print("我的爱好是{0}".format(hobby))

    print("*" *30)

    for i in args:
        print(i)

    print("*" *50)

    for k,v in kwargs:
        print(k,"---",v)
    
name="chuan"
age=18

stu(name, age)
stu(name, age,hobby="游泳")


# #收集参数的解包问题
# -把参数放入list或者字典中，或者把list/dict中的值放入收集参数中

# In[45]:


def stu(*args):
    print("哈哈哈哈哈")
    for i in args:
        print(i)

stu(1,2,3,4,5)


# #函数文档
# -函数的文档的作用是对当前函数提供使用相关的参考信息
# -文档的写法：
#     -在函数内部开始的第一行使用三引号字符串定义符
#     -一般具有特定格式
# -文档查看
#     -使用help函数，形如help(func)
#     -使用__doc__

# In[89]:


def stu(name,age,*args):
    '''
    这是文档
    '''      #更推崇使用三字符串
print("this is hanshu stu")


# In[86]:


help(stu)


# In[90]:


stu.__doc__

