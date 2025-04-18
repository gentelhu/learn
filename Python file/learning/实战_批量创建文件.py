import random
import os
import os.path

#函数编程
def create_filename():
    filename_list=[]
    lit=['水果','蔬菜','烟酒','肉蛋','粮油']
    code=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    for i in range(1,13):#创建12个文件
        filename=''
        if i<10:#小于10的文件名前面加一个0
            filename+='0'+str(i)
        else:
            filename+=str(i)
        #物资的类别
        filename+= '_'+random.choice(lit)
        #拼接识别码
        s=''
        for item in range(9):
            s+=random.choice(code)
        filename+='_'+s
        filename_list.append(filename)
    return  filename_list
#创建文件
def create_file(filename):
    with open(filename,'w') as file:
        pass

if __name__ == '__main__':
    # 指定创建文件的目录
    path='./txt/批量创建文件'
    # 创建批量创建的目录
    if not os.path.exists(path):
        os.mkdir(path)
    lst=create_filename()#获取文件名

    for item in lst:#批量生成文件
        create_file(os.path.join(path,item)+'.txt')
    # print(create_filename())


