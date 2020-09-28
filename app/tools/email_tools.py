# coding:utf8
from smtplib import SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText

from app.tools.config_tools import get_config, APP_CONFIG


def send_email(to, subject, text):
    config = get_config(APP_CONFIG)['EMAIL']
    mail_info = {
        "from": config['EMAIL_FROM'],
        "to": to,
        "host": config['EMAIL_HOST'],
        "username": config['EMAIL_USERNAME'],
        "password": config['EMAIL_PASSWORD'],
        "subject": subject,
        "text": text,
        "encoding": "utf-8"
    }
    smtp = SMTP_SSL(mail_info["host"])
    smtp.set_debuglevel(1)
    smtp.ehlo(mail_info["host"])
    smtp.login(mail_info["username"], mail_info["password"])
    msg = MIMEText(mail_info["text"], "plain", mail_info["encoding"])
    msg["Subject"] = Header(mail_info["subject"], mail_info["encoding"])
    msg["from"] = mail_info["from"]
    msg["to"] = mail_info["to"]
    smtp.sendmail(mail_info["from"], mail_info["to"], msg.as_string())
    smtp.quit()
