with open("b.txt","r",encoding="utf-8") as f:
    lines = f.readlines()
    lines2 = [line.rstrip()+" #"+str(index)+"\n" for index,line in zip(range(1,len(lines)+1),lines)]
with open("b.txt","w",encoding="utf-8") as f:
    f.writelines(lines2)
