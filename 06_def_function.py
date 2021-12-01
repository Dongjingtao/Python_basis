# 1. 函数的定义与调用（命名var, my_var）
#     def function_name(parameters):
#         """
#         docs for ‘function_name’
#         """
#         pass
#         pass
#         return parameters
#     function_name(x)
# 2. 函数参数的类型与作用
#     参数传递方式
#         假设定义了函数f(x1, x2, x3)
#             按顺序传参 f(1, 2, 3),x1=1, x2=2, x3=3
#             按名字传参 f(x1=1, x3=3, x2=2),x1=1, x2=2, x3=3
#         假设定义了函数f(x1, x2, x3=4)
#             默认传参
#                 f(x1=1, x2=2, x3=3),x1=1, x2=2, x3=3
#                 f(x1=1, x2=2),x1=1, x2=2, x3=4
#         不定长传参（*args, **kwargs）
#             def print_me(arg1, *args) args看成元组
#                 print_me(10, 70, 60)
#             def print_keyword_args(arg1, *kwargs) kwargs看成字典
#                 print_keyword_args(1, a=100, b=200)
# 3. 可变对象与不可变对象（默认参数必须指向不可变对象或类型！）
#     可变对象（列表，字典）
#     不可变对象（数值型，字符串，元组，None…）
#     例子
#         def func(num=[]):
#             num.append(0)
#             print(num)  # [0] [0, 0] [0, 0, 0]
#         def func(num=None):
#             if num is None:
#                 num = []
#             num.append(0)
#             print(num)  # [0] [0] [0]
#         func()
#         func()
#         func()
# 4. 作用域（局部变量和全局变量）
# 5. 使用内嵌函数lambda
#     f = lambda x, y: x+y
#     print(f(10, 20))
# 6. map/reduce
#     map(函数, 序列)
#         例子
#             num = list(range(10))
#             square_num = map(lambda x: x*x, num)
#             print(list(square_num))  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
#     reduce(函数, 序列)
#         例子
#             from functools import reduce
#             result = reduce(lambda x, y: x+y, [47, 11, 42, 13])
#             print(list(result))  # 113
#     filter(函数, 序列)
