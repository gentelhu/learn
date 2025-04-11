from PIL import Image
#加载图片
im=Image.open('image/google.PNG')
# print(im)
#提取RGB图像的颜色通道
r,g,b=im.split()
# print(r,g,b)
#合并通道
om=Image.merge(mode='RGB',bands=(r,b,g))
om.save('image/new_google.jpg')

