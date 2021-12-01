# 1. os模块（import os）
#     条件类
#         os.path.isdir(path)       判断path是否一个目录
#         os.path.isfile(path)      判断path是否一个文件
#         os.path.exists(path)      判断path是否存在
#         os.path.split(path)       分割文件名与目录
#         os.path.splitext(path)    分割文件名与扩展名 extension
#         os.path.join(path, name)  连接目录与文件名或目录
#         os.path.dirname(path)     返回文件所在目录
#         os.path.basename(path)    返回文件名
#         os.path.abspath(path)     得到path的绝对路径
#         os.path.getsize(path)     得到文件大小，如果path是目录返回0
#     遍历路径
#         os.listdir(path=".")      返回当前目录下的文件和文件夹
#         os.scandir(path=".")
#         os.walk(path=".")         返回(根目录), [文件夹], [文件名]
#     创建目录
#         os.mkdir(path)            如果目录已存在，报错
#         os.mkdirs(path)           递归地创建目录，一层一层地将不存在的都创建
#     删除目录
# 2. shutil模块（常用于拷贝文件，移动文件，重命名文件）
#         shutil.copy(src, dst)         复制文件内容，source,destination
#         shutil.copy2(src, dst)        复制文件内容及状态信息
#         shutil.move(src, dst)         移动文件，如果移动到相同文件夹下相当于重命名

