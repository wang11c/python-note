#!/usr/bin/env python
# coding: utf-8

# 函数作用域和集合列表字典元组
# #变量作用域
# -变量有作用范围限制
# -分类：按照作用域分类
#     -全局(global)：在函数外部定义
#     -局部(local):在函数内部定义
# -变量作用范围：
#     -全局变量：在整个全局范围都有效
#     -全局变量在局部都可以使用
#     -局部变量在局部范围可以使用
#     -局部变量在全局范围无法使用
# -LEGB原则
#     -L(local)局部作用域
#     -E(enclosing function locale)外部嵌套函数作用域
#     -G(global module)函数定义所在模块作用域
#     -B(buldin):python内置魔抗的作用域

# In[35]:


a1=100  #a1是全局的
def fun():
    print(a)
    print("I am in fun")
    a2=99  #a2作用的范围是fun
    
print(a1)
print(a2) #a2是局部的，调不出来


# eval()函数
# -把一个字符串当成一个表达式来执行，返回表达式执行后的结果
# -语法：
# 
#     eval(string_code, global=None, locals=None)

# In[47]:


x=100
y=200
z1=x+y
z2=eval("x+y") #当成代码执行

print(z1)
print(z2)


# exec()函数
# -和eval功能类似，但是不返回结果
# -语法：
#      eval(string_code, global=None, locals=None)

# In[53]:


x=100
y=200
z1=x+y
z2=exec("x+y") 
z3=exec("print('x+y:',x+y)")

print(z1)
print(z2)
print(z3)


# 递归函数
# -函数直接或者间接调用自身
# -优点：简洁，理解容易
# -缺点：对递归深度有限制，消耗资源大
# -python对递归深度有限制，超过限度报错
# -在写递归程序的时候，一定要注意结束条件

# In[56]:


#递归调用深度限制代码
x=0
def fun():
    global x
    x+=1
    print(x)
    #函数调用自己
    fun()
    
#调用函数
fun()


# In[58]:


#斐波那契数列 f1=1,f2=1,fn=f(n-1)+f(n-2)
def fib(n):  #n是第n个斐波那契数列的值
    if n==1:
        return 1
    if n==2:
        return 1

    return fib(n-1)+fib(n-2)

print(fib(15))


# 内置数据结构（变量类型）
# -list
# -set 
# -dict
# -tuple

# list 列表：
# -一组有顺序的数据的组合
# -创建列表
#     空列表

# In[61]:


#创建空列表
l1=[]
print(type(l1))

#创建带值列表
l2=[100]
print(type(l2))


# 列表常见操作
# -访问
#     -使用下标操作（索引）
# -分片操作
#     -对列表进行任意一段的截取
#     -l[:]

# In[5]:


l=[1,2,3,4,5,6,7]  #位置从0开始
l[4]


# In[6]:


l[1:3] #包前不包后


# In[67]:


l[1:4:2] #每次隔一个


# In[1]:


#数组最后一个下标是-1，从右往左-1，-2，-3，-4,...


# In[7]:


print(l)


# In[9]:


print(l[-2:-4])
#显示为空是因为分片默认从左向右截取，所以左边值要小于右边值


# In[11]:


print(l[-5:-4])


# In[13]:


#如果非得从右往左
print(l[-2:-4:-1])
#结果也是从右往左的顺序


# In[14]:


##分片操作是生成了一个新的List


# #汉诺塔问题  递归
# -规则
# 1.每次移动一个盘子
# 2.任何时候大盘子在下面，小盘子在上面
# -方法
# 1. n=1: 直接把A上的一个盘子移动到C上，A->C
# 2. n=2: 
#     1.把小盘子从A放到B上，A->B
#     2.把大盘子从A放到C上，A->C
#     3.把小盘子从B放到C上，B->C
# 3. n=3:
#     1.把A上的两个盘子，通过C移动到B上去
#     2.把A上剩下的一个最大盘子移动到C上，A->C
#     3.把B上两个盘子，借助于A，挪到C上去
# 4. n=n:
#     1.把A上的n-1个盘子，借助于C，移动到B上去
#     2.把A上的最大盘子，也是唯一一个，移动到C上，A->C
#     3.把B上的n-1个盘子，借助于A，移动到C上

# In[22]:


def hano(n,a,b,c):
    '''
    n代表几个盘子，a到c代表第1-3个塔
    '''
    if n==1:
        print(a,"->",c)
        return None  #结束的意思
    if n==2:
        print(a,"->",b)
        print(a,"->",c)
        print(b,"->",c)
        return None
    #第一步，把n-1个盘子，从a塔借助于c塔，挪到b塔上去
    hano(n-1,a,c,b)
    print(a,"->",c)
    #把n-1个盘子，从b塔，借助于a塔，挪到c塔上去
    hano(n-1,b,a,c)
a="A"
b="B"
c="C"

n=1
hano(n,a,b,c)


# In[23]:


n=2
hano(n,a,b,c)


# In[25]:


n=3
hano(n,a,b,c)


# list列表
# -del 删除

# In[27]:


a=[1,2,3,4,5]
del a[2]  #删除生成了一个新的List
print(a)


# In[29]:


del a
print(a)
#一个变量删除后不能再使用此变量


# 列表相加
# -使用加号链接两个列表

# In[1]:


a=[1,2,3,4]
b=[5,6,7]
c=a+b
print(c)


# In[3]:


#乘数就是把几个连在一起
a=[1,2,3,4,5]
b=a*3
b


# In[7]:


#成员资格运算，就是判断一个元素是否在一个List里面
a=[1,2,3,4]
b=8

c=b in a
print(c)


# In[9]:


#not in
a=[1,2,3,4]
b=8

c=b not in a
print(c)


# 列表的遍历
# for
# while

# In[11]:


a=[1,2,3,4,5]
for i in a:
    print(i)


# In[13]:


for i in range(1,10):
    print(i)


# In[23]:


#while循环访问list
#一般不用while循环遍历list


# In[26]:


#双层列表循环
#a为嵌套列表，或者叫双层列表
a=[["one",1],["two",2],["three",3]]
for k,v in a:
    print(k,"---",v)
#这个例子说明，k,v的个数应该跟变量个数一致


# In[27]:


#列表内涵:list content
#通过简单方法创作列表


# In[29]:


a=["a","b","c"]
b=[i for i in a] #对于所有a中的元素，逐个放入新列表b中
print(b)


# In[31]:


a=["a","b","c"]
b=[i*10 for i in a] 
print(b)


# In[34]:


a=[1,2,3]
b=[i*10 for i in a] 
print(b)


# In[37]:


#还可以过滤原来list中的内容放入新列表
#把偶数生成新的列表
a=[x for x in range(1,35)]
b=[m for m in a if m%2==0]
print(b)


# In[46]:


#列表生成式可以嵌套
#由两个列表a,b
a=[i for i in range(1,4)]
print(a)

b=[i for i in range(100,1000) if i%100==0]
print(b)

c=[m+n for m in a for n in b]
print(c)
#相当于
for m in a:
    for n in b:
        print(m+n, end=" ")


# In[52]:


#关于列表的常用函数
a=[x for x in range(1,100)]
print(len(a))
#len:求列表长度
#max:求列表最大值
print(max(a))
b=["i","love","python"]
print(max(b))


# In[54]:


#将其他格式传入list
a=[1,2,3]
print(list(a))


# In[56]:


s="I love you"
print(list(s)) #转列表


# In[59]:


print(list(range(12,19)))

