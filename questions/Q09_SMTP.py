# -*- coding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time


def email_Send(address):
    mail_host = "smtp.qq.com"  # 设置服务器（TX的服务器）
    mail_user = "872480366@qq.com"  # 用户名
    mail_pass = "gcveyphsdlbdbbic"  # 口令 （QQ邮箱内部授权码）

    sender = '872480366@qq.com'    # 发送人邮件地址
    receivers = [address]  # 接收人邮件地址
    # message_content = """
    # <p>我发了一张图片在里面，您可以看看哦</p>
    # <p><a href="https://image.baidu.com/search/detail?ct=503316480&z=undefined&tn=baiduimagedetail&ipn=d&word=%E7%8C%AA&step_word=&ie=utf-8&in=&cl=undefined&lm=undefined&st=undefined&hd=undefined&latest=undefined&copyright=undefined&cs=4072727232,529699927&os=1485566738,3600338637&simid=2128297322,1043379119&pn=2&rn=1&di=207920&ln=1784&fr=&fmq=1545555076136_R&fm=&ic=undefined&s=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&is=0,0&istype=0&ist=&jit=&bdtype=13&spn=0&pi=0&gsm=0&objurl=http%3A%2F%2Fimgsrc.baidu.com%2Fimgad%2Fpic%2Fitem%2Fd058ccbf6c81800a4939ed28bb3533fa828b4733.jpg&rpstart=0&rpnum=0&adpicid=0">您最近在pyq发过最好看的照片</a></p>
    # <p>↑点击查看哦↑</p>
    # """
    # message_content = """
    # <p>恭喜斗鱼ID:加内特的小内内，小哥哥您中奖了哦~感谢您一如既往的支持哦~ 比心心❤</p>
    # <p><a href="https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=%E5%91%A8%E6%B7%91%E6%80%A1&step_word=&hs=0&pn=1&spn=0&di=39600&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=0&ie=utf-8&oe=utf-8&in=&cl=undefined&lm=undefined&st=undefined&cs=312536623%2C2733272779&os=2048211120%2C1987170686&simid=0%2C0&adpicid=0&lpn=0&ln=1576&fr=&fmq=1545561821545_R&fm=&ic=undefined&s=undefined&hd=undefined&latest=undefined&copyright=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=http%3A%2F%2Fyouxi899.com%2Fwp-content%2Fuploads%2F2018%2F06%2F1212.jpg&fromurl=ippr_z2C%24qAzdH3FAzdH3Fojtk5_z%26e3Bv54AzdH3Fppw6ptvsjAzdH3FrAzdH3Ffi5o%3Ft1%3Ddnal9a9d9bclc9c80lnnnl&gsm=0&rpstart=0&rpnum=0&islist=&querylist=">点击领取一个你爱的淑仪哦~❥(^_-)</a></p>
    #
    # """

    message_content = """<p>this is a test, very nice to see u!</p>"""
    from_header = "Robot_man"                                    # 发送方名称
    receiver_call = "hello"                                # 接收方名称
    subject = 'TEST01'                     # 主题
    message = MIMEText(message_content, 'html', 'utf-8')         # HTML（超文本标记语言） 或者 plain（纯文本） 按照内容格式选择
    message['From'] = Header(from_header, 'utf-8')
    message['To'] = Header(receiver_call, 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')


    # 异常处理
    try:
        smtpObj = smtplib.SMTP()                               # 实例化一个 SMTP 对象
        smtpObj.connect(mail_host, 25)                             # 25 为 SMTP 的端口号（计算机网络有讲过哦）
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")


start = time.clock()
file = 'lkj.txt'            #邮箱记事本
f = open(file, "r+")
cnt = len(f.readlines())
f.close()
f = open(file, "r+")
for i in range(cnt):
    addr = next(f)
    email_Send(addr)
elapsed = (time.clock() - start)
print("群发成功! 用时："+str(elapsed)+"秒")