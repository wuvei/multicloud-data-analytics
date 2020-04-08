# -*- coding:utf-8 -*-

import smtplib
import base64
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.utils import COMMASPACE

SENDER = 'simonzyc40@gmail.com'
SMTP_SERVER = 'smtp.gmail.com'
USER_ACCOUNT = {'username':'simonzyc40@gmail.com', 'password':'1step1time'}
SUBJECT = "All job finished"


def send_mail(receivers, text, sender=SENDER, user_account=USER_ACCOUNT, subject=SUBJECT):
    msg_root = MIMEMultipart()  # create an instance with attachment
    msg_root['Subject'] = subject  # subject
    msg_root['To'] = COMMASPACE.join(receivers)  # receivers
    msg_text = MIMEText(text, 'html', 'utf-8')  # mail content
    msg_root.attach(msg_text)  # attach text content

    smtp = smtplib.SMTP('smtp.gmail.com:587')
    smtp.ehlo()
    smtp.starttls()
    smtp.login(user_account['username'], user_account['password'])
    smtp.sendmail(sender, receivers, msg_root.as_string())

if __name__=="__main__":
    text = 'All spark jobs were finished successfully! '
    send_mail(['yzhengbj@connect.ust.hk'], text)