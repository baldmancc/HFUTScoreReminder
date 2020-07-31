from time import sleep
from requests_html import HTMLSession

url = r'http://jxglstu.hfut.edu.cn/eams5-student/for-std/grade/sheet/info/138052?semester='
cookie_str = r'your cookies'

def str2cookies(str):
    cookies = {}
    for line in cookie_str.split(';'):
        key, value = line.split('=', 1)
        cookies[key] = value
    return cookies

def sendmail(head, text):
    import smtplib
    from email.mime.text import MIMEText
    from email.header import Header
    sender = "sender's email address"
    sender_key = "sender's email key"
    receiver = "receiver's email address"
    smtp = smtplib.SMTP() 
    smtp.connect('smtp.xxx.com',25) 
    smtp.login(sender, sender_key)   
    msg = MIMEText(text,'plain', 'utf-8')
    msg['From'] = Header(sender)
    msg['To'] = Header(receiver)
    msg['Subject'] = Header(head)
    smtp.sendmail(sender,receiver, msg.as_string())
    print('发送成功')
    smtp.quit()
    
if __name__ == '__main__':
    session = HTMLSession()
    resp = session.get(url=url ,cookies=str2cookies(cookie_str));
    subjects = resp.html.xpath(r'/html/body/div/div[1]/div[2]/table/tbody/tr')
    score = {}
    while True:
        resp = session.get(url=url ,cookies=str2cookies(cookie_str))
        subjects = resp.html.xpath(r'/html/body/div/div[1]/div[2]/table/tbody/tr')
        new = {}
        for subject in subjects:
            sub_td = subject.text.split('\n')   # 每行分列
            if sub_td[0] not in score:
                score[sub_td[0]] = sub_td[5]
                new[sub_td[0]] = sub_td[5]
        if new!={}:
            text = ''
            for k in new:
                text += (k+':'+score[k]+'\n')
            sendmail('成绩出来了', text)        
