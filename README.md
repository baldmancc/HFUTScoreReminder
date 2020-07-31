# HFUTScoreReminder

### 简介

​	爬取教务成绩，通过python自带的smtplib库发送邮件，提醒成绩出新

###　用法

1. 浏览器打开开发者模式，找到network（谷歌浏览器），正常登录，抓包，获取登录cookies在ScoreReminder.py文件中修改对应cookies。
2. 查询你常用的邮箱如何打开POP3/SMTP服务。将发送者的邮箱地址，获得的授权码，以及接收者的邮箱地址在在ScoreReminder.py文件中对应位置修改。
3. 运行程序。



### Doing

1. 解决有些云服务器25端口被屏蔽的情况
2. 可以通过教务的账户密码登录

### Next

1. 可能会新增其他功能

