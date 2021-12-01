# 1. 类与对象（人类认识世界的哲学之一）（命名Class, MyClass）
#     概念
#         认识世界的基本方法： 分类（class）
#         分类的结果是，我们拥有了不同的： 类别或类型
#         最终我们通过分类的方法，对所处的世界建立了： 概念
#         python中已有的类型（int, float, list, tuple）
#         可以转换类型（float(5) -> 5.0  list((1, 2, 3)) -> [1, 2, 3]）
#         面向对象编程，Object-oriented Programming，简称OOP
#     自定义类型
#         #定义
#         class Student(object):
#             def __init__(self, name, score):
#                 self.name = name
#                 self.score = score
#             def print_score(self):
#                 print('%s: %s' % (self.name, self.score))
#         #调用
#         you = Student("Ramon", 100)
#         you.print_score()
# 2. __init__方法
#     self.name = name  # 对象的属性=值
#     self.__score = score  # 私有属性，外部无法访问
#         you.__score          # 外部无法访问
#         you._Student__score  # 外部可以访问，原则上不合适
#         def get_score(self):
#             return self.__score
#         your_score = you.get_score()  # 外部获取私有属性的值
# 3. 对象的方法
#     print_score()
