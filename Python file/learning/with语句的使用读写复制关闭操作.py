def write_fun():
    with open('txt/aa.txt','a',encoding='utf-8') as file:
        file.write('冬奥会')
def read_fun():
    with open('txt/aa.txt', 'r', encoding='utf-8') as file:
        print(file.read())
def copy_fun(src_file,target_file):
    with open(src_file, 'r', encoding='utf-8') as file:
        with open(target_file, 'w', encoding='utf-8') as file2:
            file2.write(file.read())#将读取的文件直接写入文件
if __name__ == '__main__':
    write_fun()
    read_fun()
    copy_fun('txt/aa.txt','txt/bb.txt')