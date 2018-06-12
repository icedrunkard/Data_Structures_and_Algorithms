"""-------------------开始测试类的装饰器---------------------"""
# class myDecorator(object):
#
#     def __init__(self, f):
#         print("inside myDecorator.__init__()")
#         f() # Prove that function definition has completed
#
#     def __call__(self):
#         print("inside myDecorator.__call__()")
#
# @myDecorator
# def aFunction():
#     print("inside aFunction()")
# print('----------- 以上在初始化 -----------------')
# aFunction()
# print("-----------------Finished decorating aFunction()-------------")


"""--------------------开始测试@property----------------------------"""

# class Student(object):
#     _score = None
#
#     # 比如直接对stu.score 进行赋值，范围可以999，不合理
#     # 让方法变成属性调用的好处是，可以对属性进行一些条件选择，可以设置
#
#     @property
#     def score(self):
#         return self._score
#
#     @wraps
#     @score.setter  # 具有了修改的权限
#     def score(self, value):
#         if value < 0 or value > 100:
#             raise ValueError('分数不在合理范围')
#         self._score = value
#
#
# stu = Student()
# print(stu.score)
# stu.score = 99
# print(stu.score)


"""--------------------开始测试函数装饰器----------------------------"""
import time
from functools import wraps  # 可以保留
def timer(func):
    # @wraps(func)
    def inner(*args,**kwargs):
        print('function name is:',func.__name__)
        print('function doc is:', func.__doc__)
        t0=time.time()
        func(*args,**kwargs)
        t1=time.time()
        print('time cost: {}s'.format(t1-t0))
    return inner


@timer
def sleep(t):
    """ready to sleep..."""
    time.sleep(t)
sleep(1)
