import os.path
print('获取目录或文件的绝对路径:',os.path.abspath('./bbb.py'))
print('判断目录或文件在磁盘上是否存在:',os.path.exists('./bbb.py'))
print('判断目录或文件在磁盘上是否存在:',os.path.exists('./txt'))
print('将目录与目录名或文件名进行拼接:',os.path.join('F:\gentel\learn\system\Python file\learning','bbb.py'))
print('分别获取文件名和后缀名:',os.path.splitext('bbb.py'))
print('从path中提取文件名:',os.path.basename(r'F:\gentel\learn\system\Python file\learning\bbb.py'))
print('从path中提取路径（不包含文件名）:',os.path.dirname(r'F:\gentel\learn\system\Python file\learning\bbb.py'))
print('判断path是否是有效路径:',os.path.isdir(r'F:\gentel\learn\system\Python file\learning'))
print('判断file是否是有效文件:',os.path.isfile(r'F:\gentel\learn\system\Python file\learning\bbb.py'))


