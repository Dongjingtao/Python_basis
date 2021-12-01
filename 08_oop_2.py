# 1. return和yield
#     return和print的区别
#         return的含义是函数返回值，是函数的出口，一般只用一次，后面的return无法到达
#         print在同一函数中可以使用多次
#     return多个值
#         def return_multi_value(x1, x2):
#             return x1 + x2, x1 - x2, x1 * x2, x1 / x2
#         result1 = return_multi_value(1, 2)  # 返回一个元组(3, -1, 2, 0.5)
#         _, _, _, result2 = return_multi_value(1, 2)  # 0.5
#     return的缺陷（数据量过大时）
#         def process(data):
#             result = []
#             for i in data:
#                 result.append(i)
#             return result
#     yield与return的区别（不一次性返回所有结果）
#         例子
#             def process_alter(data):
#                 for i in data:
#                     yield i
#             gen = process_alter([1, 2, 3])  # 返回生成器
#             print(next(gen))  # 1
#             print(next(gen))  # 2
#             print(next(gen))  # 3
#     迭代器与生成器（Iterator & Generator）
#         *可迭代对象iterable（具有可迭代属性的对象，如列表，字典，字符串等）
#             判断是否可迭代
#                 from collections import Iterable
#                 print(isinstance(range(5), Iterable))  # True
#             *迭代器（一类特殊的可迭代对象，迭代可迭代对象的对象，有迭代能力）
#                 my_iterator = iter([1, 2, 3])  # 使用iter()把可迭代对象变成迭代器
#                 next(my_iterator)              # 使用next()不断获取下一个数据，直到出现StopIteration错误
#                 例子
#                     def __iter__(self):
#                         return self            # 相当于iter()
#                     def __next__(self):
#                         self.number = self.number + 1
#                         return self.number     # 相当于next()
#                 迭代器可以表示一个无限大的数据流，例如全体自然数，而可迭代对象不行
#                 判断是否为迭代器
#                     from collections import Iterator
#                     print(isinstance(range(5), Iterator))  # False
#                 *生成器（一类特殊的迭代器）
#                     将函数变为生成器
#                         在函数中用yield，若只有一个结果，不如用return
#                     生成器表达式
#                         gen = ( x**2 for x in range(0, 10))也是一个生成器
# 2. 继承和多态（ class 子类名(父类名) ）
#     获得父类的所有方法
#     获得改进代码的可能性  # 多态（一个函数名，多种状态或效果）
#     继承父类的属性
#         class Vehicle(object):
#             def __init__(self, speed):
#                 self.speed = speed
#         class Helicopter(Vehicle):
#             def __init__(self, speed):
#                 super().__init__(speed)  # super()继承父类属性
#             def driving(self):
#                 print("Speed : %s" % self.speed)
#         bird = Helicopter(200)
#         bird.driving()



