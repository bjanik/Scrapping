import os
import smtplib
import ssl

from dotenv import load_dotenv
from email.mime.text import MIMEText

load_dotenv()
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

def send_email():
    msg = MIMEText("Poker all time money ranking was updated, check hendonmob.com", 'html')
    msg['Subject'] = 'Poker rankings'
    msg['From'] = EMAIL
    msg['To'] = EMAIL

    s = smtplib.SMTP_SSL(host='smtp.gmail.com', port = 465)
    s.login(user=EMAIL, password=PASSWORD)
    s.sendmail(EMAIL, EMAIL, msg.as_string())
    s.quit()
