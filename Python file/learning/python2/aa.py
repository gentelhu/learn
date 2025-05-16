import io
s = "hello, sxt"
sio = io.StringIO(s)   #可变字符串
print(sio)
v1 = sio.getvalue()
print("v1:",v1)
char7 = sio.seek(7)    #指针知道索引7这个位置
sio.write("gaoqi")
v2 = sio.getvalue()
print("v2:",v2)
