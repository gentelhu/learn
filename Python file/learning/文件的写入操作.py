def my_write(s):
    file=open('txt/b.txt','a',encoding='uft-8')#打开文件追加模式
    file.write(s)#写入s
    file.write('\n')#写入换行
    file.close()#关闭文件
def my_write_list(file,lst):
    f=open(file,'a',encoding='utf-8')
    #操作文件
    f.writelines(lst)
    f.close()

#主程序运行
if __name__ == '__main__':#输入main按tab键可以自动补全
    # my_write('伟大的中国梦')
    # my_write('北京欢迎你')
    lst=['姓名\t','年龄\t','成绩\n','张三\t','30\t','98']
    my_write_list('txt/c.txt',lst)




