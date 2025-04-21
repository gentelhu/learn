def find_answer(question):
    with open('./txt/automatic_reply.txt','r',encoding='utf-8') as file:
        while True:
            line=file.readline()
            if line=='':
                break
            # 分割字符串
            parts = line.split('|')
            if len(parts) > 1:
                keyword = parts[0]
                reply = parts[1]
            if keyword in question:
                return reply
    return False

if __name__ == '__main__':
    question=input("Hi.XXX你好，小蜜在此等主人很长时间了，有什么麻烦和小蜜说说吧：")
    while True:
        if question=='BEY':
            break
        else:
            reply=find_answer(question)#返回值有两种可能找到答案为True，找不到为Flase
            if reply==False:#没有答案
                question=input('小蜜不知道您在说什么，您可以问我一些，订单、物流、账户、支付方面的问题，退出请输BEY：').upper()
            else:
                print(reply)
                question=input('小主您还可以问一些关于订单、物流、账户、支付方面的问题，退出请输BEY：').upper()
    print('小主再见')

