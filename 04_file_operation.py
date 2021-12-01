# 1.文件的读写
#     路径
#         绝对路径（完整的路径，表示路径在""内使用/或\\或者在""外使用r""，如果用\容易使路径产生转义字符）
#         相对路径（"./"表示同一层，"../"表示上一层）
#     打开文件
#         函数open(filename, mode="r", encoding=None)
#     读取数据（假设f = open（…））
#         f.read()      一次读取全部内容，重复调用read(size)每次最多读取size个字节的内容
#         f.readline()  每次读取一行内容
#         f.readlines() 一次读取全部内容并按行返回list
#     关闭文件（假设f = open（…））
#         f.close()
#     花式读文件
#         with open(…) as f:
#           # do something
#           # 自动关闭文件
#     模式（mode）
#         r 只读
#         w 只写（可能创建新文件）
#         a 追加（文件指针在最后，可能创建新文件）
#         x 不存在文件时创建（存在文件时失败）
#         + 读写（不能单独使用）
#         b 以二进制形式打开
# 2.txt文件读取（统一UTF-8编码）
#      确定文件的编码
#          from chardet import detect
#          contents = open("class.txt", "rb").read()
#          print(detect(contents))
# 3.csv文件读取（逗号分隔值的文件格式，像表格）
# 4.文件输出（mode="w"，保证有换行符\n）
# 5.使用JSON处理数据（字典式是数据结构，像字典）
#     需要使用Python标准库：json
#         import json
#     四种方法
#         例子
#             data = {
#                 '名字': '学员X',
#                 '身份': '小可爱',
#                 '身高(cm)': 185
#             }
#             针对字符串(str)
#                 json.dumps()  # 数据变成字符串(unicode,utf-8)
#                     json_str = json.dumps(data)
#                 json.loads()  # 字符串加载成新数据
#                     new_data = json.loads(json_str)
#             针对文件
#                 json.dump()  # 序列化Serialization，数据以json格式保存到文件中(unicode)，以二进制形式写入文件，保存到硬盘中
#                     with open('data.json', 'w') as f:
#                         json.dump(data, f, indent=4)
#                 json.load()  # 反序列化Deserialization，序列化的逆操作
#                     with open('data.json', 'r') as f:
#                         new_data = json.load(f)
#                 例子
#                     import pickle
#                     a = [1, 2, 3]

