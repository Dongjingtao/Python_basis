# 1. 推导式 Comprehension（ 括号，想要收集的元素，循环，条件过滤（可不写） ）
#     列表推导式 List Comprehension
#         [x for x in range(10) if x % 2 == 0]
#     集合推导式 Set Comprehension
#         {x for x in range(10) if x % 2 == 0}
#     字典推导式 Dict Comprehension
#         {x: x**2 for x in range(10) if x % 2 == 0}
#     生成器表达式 Generator Expression
#         (x for x in range(10) if x % 2 == 0)
#     检查
#         print(x)  print(type(x)) print(isinstance(x, class))
# 2. 异常处理 try-except-else-finally
#     内置错误类型（FileExistsError，FileNotFoundError，StopIteration，ImportError，…)
#         Exception（常规错误的父类）
#         BaseException（内置错误的父类）
#         异常也是对象（类），一切皆对象
#         官方文档：http://docs.python.org/3/library/exceptions.html#bltin-exceptions
#     有异常要处理
#         例子1（最简单的）
#             x = list(range(10))                           # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#             try:
#                 a = x[10]
#             except Exception:
#                 print("what the hell?")                   # what the hell?
#         例子2
#             x = list(range(10))
#             try:
#                 a = x[10]
#             except Exception as error:
#                 print(isinstance(error, BaseException))   # True
#         例子3（把错误内容打印出来）
#             x = list(range(10))
#             try:
#                 a = x[10]
#             except IndexError as error:
#                 print(error)                                  # list index out of range
#         例子4
#             x = list(range(10))
#             try:
#                 a = x[9]
#                 print(b)
#             except IndexError as idx_error:
#                 print(idx_error)
#             except NameError as name_error:
#                 print(name_error)                              # name 'b' is not defined
#         例子5
#             try:
#                 f = open("testfile", "w", encoding="ASCII")
#                 f.write("这是一个测试文件，用于测试异常！")
#             except IOError:
#                 print("Oops...")
#             else:
#                 print("OK")
#                 f.close()
#         例子6
#             def test(a, b):
#                 try:
#                     result = a /b
#                     print(result)
#                 except ZeroDivisionError as error:
#                     print(error)
#                 else:
#                     print("test")
#                 finally:
#                     print("test finally keyword")
# 3. 深浅拷贝
#     python中保存的是变量的值
#     例子
#         from copy import copy, deepcopy
#         a = [1, ["a", "b"]]
#         b = a
#         c = copy(a)      # 浅拷贝：只能保证外层对象不被修改
#         d = deepcopy(a)  # 深拷贝：完全拷贝，内外层都不会被修改
#         a.append(5)
#         a[1].append("c")
#         print(a)  # a=[1, ["a", "b", "c"], 5]
#         print(b)  # b=[1, ["a", "b", "c"], 5]
#         print(c)  # c=[1, ["a", "b", "c"]]
#         print(d)  # d=[1, ["a", "b"]]
# 4.数据处理的花招
#     Unpacking
#         例子
#             man = ("Ramon", "Yang", 185, "youku")
#             first_name, last_name, height, email = man
#     交换两个值
#         例子
#             a, b = b, a
#     组合字符串
#         例子
#             colors = ["red", "blue", "yellow"]
#             print(",".join(colors))
#     循环
#         例子
#             colors = ["red", "blue", "yellow"]
#             for color in colors:
#                 print(color)
#     带下标循环
#         例子
#             colors = ["red", "blue", "yellow"]
#             for idx, color in enumerate(colors):
#                 print(idx, "-->", color)
#     all & any
#         例子
#             ages = [42, 21, 18, 33, 19]
#             if all(map(lambda x: x >= 18, ages)):
#                 print('All are adults!')
#             if any(map(lambda x: x == 18, ages)):
#                 print('Found 18-year-old')
