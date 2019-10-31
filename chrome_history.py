import browserhistory as bh
import pandas as pd

dict_obj = bh.get_browserhistory
bh.write_browserhistory_csv()
df = pd.read_csv('chrome_history.csv', encoding= "utf8")
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import datetime as dt
%matplotlib inline
 
users=df.groupby('name')['date'].count().nlargest(15)
 
def bar_chart(users):
    ax = users.plot(kind='bar', color = ['red','gold','skyblue','green','orange','teal','cyan','lime','orangered','aqua'], fontsize=12)
    ax.set_title("Internet with Date Count\n", fontsize=18)
    ax.set_xlabel("Internet", fontsize=12)
    ax.set_ylabel("Date", fontsize=12)
    plt.show()
    plt.savefig('whatsapp.png')
bar_chart(users)


date = lambda x: x['date'].split(' ')[0]
df['ndate'] = df.apply(date, axis=1)
time = lambda x: x['date'].split(' ')[1:]
df['time'] = df.apply(time, axis=1)
df['time'] = df.time.apply(lambda x: ''.join([str(time) for time in x]))

df.drop('date', axis=1, inplace=True)

users=df.groupby('name')['ndate'].count().nlargest(20)
 
def bar_chart(users):
    ax = users.plot(kind='barh', color = ['red','gold','skyblue','green','orange','teal','cyan','lime','orangered','aqua'], fontsize=12)
    ax.set_title("Internet with Date Count\n", fontsize=18)
    ax.set_xlabel("Internet", fontsize=12)
    ax.set_ylabel("Date", fontsize=12)
    plt.show()
#     plt.savefig('whatsapp.png')
bar_chart(users)
a = df[df['ndate'] >= '2019-09-24']

users=a.groupby('name')['ndate'].count().nlargest(15)
 
def bar_chart(users):
    ax = users.plot(kind='bar', color = ['red','gold','skyblue','green','orange','teal','cyan','lime','orangered','aqua'], fontsize=12)
    ax.set_title("Internet with Date Count\n", fontsize=13)
    ax.set_xlabel("Internet", fontsize=12)
    ax.set_ylabel("Date", fontsize=12)
    plt.savefig('whatsapp1.png')
    plt.show()
bar_chart(users)

users=df.groupby('time')['ndate'].count().nlargest(15)
 
def bar_chart(users):
    ax = users.plot(kind='bar', color = ['red','gold','skyblue','green','orange','teal','cyan','lime','orangered','aqua'], fontsize=12)
    ax.set_title("time with Date Count\n", fontsize=13)
    ax.set_xlabel("time active", fontsize=12)
    ax.set_ylabel("Date", fontsize=12)
    plt.savefig('whatsapp2.png')
    plt.show()
bar_chart(users)

users=a.groupby('time')['ndate'].count().nlargest(15)
 
def bar_chart(users):
    ax = users.plot(kind='bar', color = ['red','gold','skyblue','green','orange','teal','cyan','lime','orangered','aqua'], fontsize=12)
    ax.set_title("time with Date Count (24-09-2019\n", fontsize=13)
    ax.set_xlabel("Internet", fontsize=12)
    ax.set_ylabel("Date", fontsize=12)
    plt.savefig('time1m.png', dpi=100)
    plt.show()
bar_chart(users)



import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

email_user = 'yourmail'
email_password = 'yourpassword'
email_send = 'who to mail to'

subject = 'python for browser history'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

body = 'Hi there, i am testing out this script by emailing myself, this script takes my browser history and plots my 15 most frequent sites against date and then time against time'
msg.attach(MIMEText(body,'plain'))

filename1 ='time1m.png'
attachment  =open(filename1,'rb')
part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename1)
msg.attach(part)

filename2 ='whatsapp1.png'
attachment  =open(filename2,'rb')
part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename2)
msg.attach(part)

filename3 ='whatsapp2.png'
attachment  =open(filename3,'rb')
part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename3)
msg.attach(part)

text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,email_password)


server.sendmail(email_user,email_send,text)
server.quit()
