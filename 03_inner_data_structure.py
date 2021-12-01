# 0. 基本问题（增删改查，切片排序，时间复杂度，空间复杂度）
# 1. 列表（可以修改，有序）
#         增 list.append(x) list.extend(iterable) list.insert(i,x)_
#         删 list.remove(x) list.pop([i]) list.clear()
#         改 list.reverse() a[i]=x
#         查 list.index(x[,start[,end]]) list.count(x)
#         切片 a[i:j]
#         列表推导式[x for x in range(0,10) if x % 2 == 0]
# 2. 元祖（不可修改，只有一个元素时(50,) ）
#         增
#         删 del tup
#         改 tup3 = tup1 + tup2
#         查 tup[0]
#         索引和切片 tup[1:]
#         运算符和内置函数（tup1= (1, 2, 3)）
#             tup1 * 3 = (1, 2, 3, 1, 2, 3, 1, 2, 3)
#             tuple([1, 2, 3]) = (1, 2, 3)
#             len max
# 3. 字符串（不可变）
#         增
#         删
#         改 s = s1+ s2
#         查 s[0]
#         索引和切片 s[1:]
#         转义字符（\ \\ \' \" \n \t）
#             \  行尾时，续行符
#             \\ \
#             \' '
#             \" "
#             \n 换行
#             \t 横向制表符
#         格式化字符串（%s）
#             print("My name is %s and weight is %s kg!"% ('Ramon', 75))
#         内置函数
#             string.capitalize()    第一个字符大写
#             string.count(str)      统计str出现次数
#             string.startswith(obj) 判断是否以obj开头
#             string.endswith(obj)   判断是否以obj结尾
#             string.split(str="", num=string.count(str)) 以str为分隔符切片string
# 4. 字典（可变，键值对内部用:分割，键值对之间用,分割，键唯一且类型不可变）
#         增 dict1[ "School" ] = "极值学院"
#         删 del dict1["Name"]  dict1.clear()  del dict1
#         改 dict1[ "Age" ] = 8
#         查 dict1[ "Alice" ]
#         内置函数
#             dict.keys()   以列表返回字典中的所有键
#             dict.values() 以列表返回字典中的所有值
#             dict.items()  以列表返回字典中的所有(键, 值)元祖
# 5. 集合（不可变，不支持索引，运算: 并| 交& 差- 异或^ ）
#         增
#         删
#         改
#         查
#         内置函数
#             set.add(x)     增加一个值
#             set.discard(x) 删除一个值
#             set.remove(x)  删除一个值（如果x不在set内，会报错）
#             set.clear()    删除所有内容
#         冷冻集合（冷冻不可变,其余与set一致）
#             fset = frozenset([1, 2, 3, 4])


