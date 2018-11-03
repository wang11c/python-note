#!/usr/bin/env python
# coding: utf-8

# In[4]:


def a(n):
    n[2] = 300
    print(n)
    return None

def b(n):
    n+=100
    print(n)
    return None

an=[1,2,3,4,5,6]
bn=9

print(an)
a(an)
print(an)

print(bn)
b(bn)
print(bn)
#同样两个函数，一个变完了后改了原函数，一个没改，改了叫传地址（复杂变了），没改叫传值（简单变量）


# In[5]:


#关于列表的函数


# In[15]:


l=['a','i love you',12,34,45,(5+4j)]
l


# In[16]:


#append 在末尾插入一个内容
a=[i for i in range(1,5)]
print(a)
a.append(100)
print(a)


# In[20]:


#insert 在指定位置插入  insert(位置,data)
a=[i for i in range(1,5)]
print(a)
a.insert(3,666)
print(a)


# In[22]:


#删除
#del
#pop,从对位拿出一个元素，即把最后一个元素取出来
a=[i for i in range(1,5)]
print(a)
last_ele=a.pop()
print(last_ele)
print(a)


# In[27]:


#remove 在列表中删除指定的值,前提是必须要有被删除的值
a=[i for i in range(1,5)]
print(a)
a.remove(2)
print(a)


# In[29]:


a=[i for i in range(1,5)]
if 2 in a:
    a.remove(2)
print(a)
#remove在原list操作


# In[30]:


#clear 清空
a=[i for i in range(1,5)]
a.clear()
print(a)


# In[32]:


#reverse 翻转列表内容，原地翻转
a=[1,3,4,5]
print(a)
print(id(a))

a.reverse()
print(a)
print(id(a))


# In[34]:


#extend 扩展列表，两个列表，把一个直接拼到后一个上
a=[1,3,4,5]
b=[6,7,8,9]
a.extend(b)
a


# In[38]:


#count 查找列表中指定值或元素的个数
a=[1,3,4,5,5]
a_len=a.count(3)
print(a_len)
#有一个3
a_len=a.count(5)
print(a_len)
#有两个5


# In[51]:


#copy 拷贝
a=[1,2,3,4,5,6,777]
b=a
b[2]=888
print(a)
print(b)
print(id(a))
print(id(b))
#用=左右地址相同

print('*'*30)

b=a.copy()
b
print(a)
print(b)
print(id(a))
print(id(b))
#copy的地址不同


# In[57]:


#浅拷贝
a=[1,2,3,[4,5,6]]
b=a.copy()

print('*'*30)

print(id(a))
print(id(b))

print('*'*30)

print(id(a[3]))
print(id(b[3]))
#但是copy里面更深一层的来源相同，地址相同

print('*'*30)

a[3][2]=666
print(a)
print(b)
#copy函数是浅拷贝，即只拷贝一层内容，改了一个就都改了


# 元组-tuple
# - 元组可以看成一个不可更改的list
# 创建元组

# In[58]:


#创建空元组
t=()
print(type(t))


# In[61]:


#创建一个只有一个值的元组
t=(1,)
print(type(t))
print(t)

m=(1)
print(type(m))
print(m)


# In[62]:


t=1,
print(type(t))
print(t)


# In[64]:


#创建多个值的元组
t=(1,2,3,4,5)
print(type(t))
print(t)


# In[65]:


#其他结构改成元组
l=[1,2,3,4,5]
t=tuple(l)
t


# 元组特点
# -是序列表，有序
# -元组数值可以访问，不能修改
# -元组数据可以是任意类型
# -list所有特性，除了可修改外，元组都有，比如索引，分片，序列相加，相乘等

# In[66]:


#索引操作
t=(1,2,3,4,5)
print(t[4])


# In[68]:


#超标错误
t=(1,2,3,4,5)
print(t[10])


# In[71]:


t=(1,2,3,4,5)
t1=t[1::2]
print(id(t))
print(id(t1))
print(t1)

#切片可以超标
t2=t[2:100]
t2


# In[74]:


#序列相加
t1=(1,2,4)
t2=(5,6,7)

#传址操作
print(t1)
print(id(t1))
t1+=t2
print(t1)
print(id(t1))
#传址操作，所以可以改,tuple的不可修改，是指内容的不可修改


# In[75]:


#元组相乘
t=(1,2,3)
t=t*3
print(t)


# In[77]:


#成员检测
t=(1,2,3) 
if 2 in t:
    print("yes")
else:
    print("no")


# In[82]:


#元组遍历，一般采用for
t=(1,2,3,"i love you")
for i in t:
    print(i,end=" ")


# In[85]:


#双层元组的遍历
t=((1,2,3),(4,5,6))
for i in t:
    print(i)
for k,m,n in t:
    print(k,"---",m,"---",n)


# In[2]:


#关于元组的函数
#len:获取元组的长度
t=(1,2,3)
len(t)


# In[4]:


#max,min:最大值最小值  如果列表或元组中有多个最大最小值，则实际打印出哪个
print(max(t))
print(min(t))


# In[8]:


#tuple:转化或创建元组
l=[1,2,3,4,5]
t=tuple(l)
print(t)


# In[ ]:


#元组的函数 基本跟list通用


# In[17]:


#count:计算指定数据出现的次数
t=(2,3,4,4,6,7,8)
print(t.count(2))

#index：求指定元素在元组中的索引位置
print(t.index(2))

#如果查找多个，则返回第一个
print(t.index(4))


# In[ ]:


#元组变量交换


# In[18]:


#两个变量交换值
a=1
b=3
a,b=b,a

print(a)
print(b)


# 集合-set
# -集合是高中数学中的一个概念
# -一对确定的无序的唯一的数据，集合中每一个数据成为一个元素

# In[19]:


#集合的定义
s=set()
print(type(s))


# In[21]:


#如果只是用大括号定义，则定义的是一个dict类型
d={}
print(type(d))


# 集合的特征 
# -集合内数据无序，无法使用索引和分片
# -集合内部数据元素具有唯一性，可以用来排除重复数据
# -集合内的数据，str,int,float,tuple，冰冻集合等

# In[26]:


#集合序列操作
#成员检测 in, not in
s={1,2,4,"i love"}
print(s)

if 1 in s:
    print("OK")

if 1 not in s:
    print("not OK")


# In[27]:


#集合便利操作
#for循环
s={1,2,4,"i love"}

for i in s:
    print(i,end="")


# In[31]:


#带有元组的集合遍历
s={(1,3,4),(2,5,6),("i","love","you")}
for k,m,n in s:
    print(k,"--",m,"--",n)


# In[ ]:





# In[35]:


#集合的内涵
#普通集合内涵
s={2323,435,654,67,345,346,7,653,3,3,3,12,56}
print(s)
#自动把重复的过滤掉了

ss={i for i in s if i%2 ==0} #挑出偶数
print(ss)


# In[37]:


#多循环的集合内涵
s1={1,2,3,4}
s2={"i","love","you"}
s={m*n for m in s2 for n in s1}
print(s)


# In[38]:


#集合函数 关于集合的函数


# In[39]:


s={32,45,567,324,23,32,32}
print(len(s))
print(max(s))
print(min(s))


# In[41]:


#set：生成一个集合
l=[1,3,4,6,7,8]
s=set(l)
print(s)


# In[43]:


#add:向集合内添加元素
s={1}
s.add(21)
print(s)


# In[44]:


#clear
s={32,45,567,324,23,32,32}
print(id(s))
s.clear()
print(id(s))
#结果表明clear原地清空数据


# In[45]:


#copy:拷贝 
#remove:移除指定的值，直接改变原有值，如果要删除的值不存在，报错  
#discard:移除集合中指定的值，如果要删除的值不存在，不报错  
s={1,2,3,4,556,7,}
s.remove(4)
print(s)

s.discard(1)
print(s)


# In[47]:


s.remove(100)
print(s)


# In[48]:


#pop:随机移除一个元素
s={1,2,3,4,556,7,}
d=s.pop()
print(d)
print(s)


# In[51]:


#集合函数
#intersection:交集
#difference:差集
#union:并集
#issubset:检查一个集合是否为另一个的子集
#issuperset:检查一个集合是否为另一个的超集
s1={1,2,3,4,5}
s2={5,6,7,8}
s_1=s1.intersection(s2)
print(s_1)

s_2=s1.difference(s2)
print(s_2)

s_3=s1.issubset(s2)
print(s_3)


# In[53]:


#frozen set:冰冻集合
#冰冻集合就是不可以进行任何修改的集合


# In[55]:


#创建
s=frozenset()
print(s)
print(type(s))


# #dict字典
# -字典是一种组合数据，没有顺序的组合数据，数据以键值对形式出现

# In[61]:


#字典的创建
#创建空字典1
d={}
print(d)

#创建空字典2
d=dict()
print(d)

#创建有值的空字典，每一组数据用冒号隔开，每一对键值用逗号隔开
d={"one":1,"two":2,"three":3}
print(d)

#用dict创建有内容字典1
d=dict({"one":1,"two":2,"three":3})
print(d)

#用dict创建有内容字典2
d=dict(one=1,two=2,three=3)
print(d)

#用dict创建有内容字典3
d=dict({("one",1),("two",2),("three",3)})
print(d)


# #字典的特征
# -字典是序列类型，但是是无序序列，所以没有分片和索引
# -字典中的数据每个都由键值对组成，即kv对
#     -key:必须是可哈希值，比如int,string,float,tuple,但是List，set，dict不行
#     -value：任何值

# In[65]:


#常见操作
#访问数据
d={"one":1,"two":2,"three":3}
#注意访问格式
#中括号内是键值
print(d["one"])

d["one"]="eins"
print(d)

#使用del操作
del d["one"]
print(d)


# In[66]:


#成员检测 in, not in
d={"one":1,"two":2,"three":3}
if 2 in d:
    print("value")
    
if "two" in d:
    print("key")

if ("two",2) in d: 
    print("kv")
#成员检测之检测的是key的内容


# In[70]:


#遍历在python2和3中区别大，代码不通用
#按key来使用for循环
d={"one":1,"two":2,"three":3}
for k in d:
    print(k, d[k])
    
#也可写成
for k in d.keys():
    print(k, d[k])
    
#只访问字典的值
for v in d.values():
    print(v)
    
#特殊用法
for k,v in d.items():
    print(k,"--",v)


# In[ ]:


#字典生成式


# In[72]:


d={"one":1,"two":2,"three":3}
dd={k:v for k,v in d.items()}
print(dd)

#加限制条件的字典生成式
dd={k:v for k,v in d.items() if v%2==0}
print(dd)


# In[73]:


#字典的相关函数


# In[74]:


#通用函数 len,max,min,dict
#str(字典)：返回字典的字符串格式
d={"one":1,"two":2,"three":3}
print(str(d))


# In[76]:


#clear:请空字典
#items:返回字典的键值对组成的元组格式

d={"one":1,"two":2,"three":3}
i=d.items()
print(type(i))
print(i)


# In[77]:


#keys:返回字典的键组成的一个结构
k=d.keys()
print(type(k))
print(k)


# In[79]:


#values:同理，一个可迭代的结构
v=d.values()
print(type(v))
print(v)


# In[86]:


#get:根据指定键返回相应的值，好处是可以设置默认值
d={"one":1,"two":2,"three":3}
print(d.get("one"))
print(d.get("one",100))  #如果没有one的值，自动设置成100
print(d.get("on22"))


# In[81]:


#get默认值是None,可以设置
print(d.get("on22",100))


# In[82]:


#fromkeys：使用一个值作为字典所有的键的值
l=["eins","zwei","drei"]
d=dict.fromkeys(l,"hahhaah")
print(d)

