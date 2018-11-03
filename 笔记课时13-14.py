#!/usr/bin/env python
# coding: utf-8

# #OOP-python面向对象
# -面向对象变成
#     -基础
#     -公有私有
#     -继承
#     -组合
# -魔法函数
#     -魔法函数概述
#     -构造类魔法函数
#     -运算类魔法函数

# # 1.面向对象概述（objectoriented.）
# -OOP思想
# -几个名词
# 	- OO：面向对象
# 	- OOA：面向对象的分析
# 	- OOD：面向对象的设计
# 	- OOI：面向对象的实现
# 	- OOP：面向对象的编程
# 	- OOA>OOD>OOI：面向对象的实现过程

# #类和对象的概念
# -类和对象的概念
# 	-类：抽象名词，代表一个集合，共性的事物
# 	-对象：具象的事物，单个个体
# 	-类跟对象的关系
# 		-一个具象，代表一类事物的某一个个体
# 		-一个是抽象，代表的是一大类事物
# -类中的内容，应该具有两个内容
# 	-表明事物的特征，叫做属性（变量）
# 	-表明事物功能或动作，成为成员方法（函数）

# In[ ]:


# 2. 类和对象的概念
- 类的命名
	-遵守变量命名的规范
	-大驼峰（由一个或者多个单词构成，每个单词首字母大写，但词根单词直接相连）
	-尽量避免跟系统命名相似的命名
-如何声明一个类
	-必须用class关键字
	-类由属性和方法构成，其他不允许出现
    -成员属性定义可以直接使用变量赋值，如果没有值，不需使用None
    -案例 01.py


# In[ ]:


#定义一个空的类
class Student():
        pass #pass必须有，定义底下必须有东西
#定义一个对象
mingyue=Student()
#定义一个类，用来描述python的学生
class PythonStudent():
    name=None #用None给不确定的值赋值
    age=18
    course="Python"

del doHomework(self):
    print("I 在做作业")
    return None #推荐在函数末尾使用return语句


# In[ ]:


#实例化一个叫yueyue的学生，是一个具体的任
yueyue=PythonStudent()
yueyue.name
yueyue.age
yueyue.doHomework()


# # 3.anaconda基本使用
# -anaconda主要是一个虚拟环境管理器
# -还是一个安装包管理器
# -conda list:显示anaconda安装的包
# -conda env list:显示anaconda的虚拟环境列表

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




