import os
import smtplib
from dotenv import load_dotenv

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

load_dotenv()

MAIL_USERNAME = os.environ.get('MAIL_USERNAME', '')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', '')
MAIL_FROM = os.environ.get('MAIL_FROM', '')
MAIL_PORT = int(os.environ.get('MAIL_PORT', 587))
MAIL_SERVER = os.environ.get('MAIL_SERVER', '')
MAIL_TLS = True if os.environ.get('MAIL_TLS', 'False') == "True" else False
MAIL_SSL = True if os.environ.get('MAIL_SSL', 'False') == "True" else False
USE_CREDENTIALS = True if os.environ.get('USE_CREDENTIALS', 'False') == "True" else False


class MailSender:

    def __init__(self, conf):
        if conf['MAIL_TLS']:
            self.session = smtplib.SMTP(host=conf['MAIL_SERVER'], port=conf['MAIL_PORT'])
            self.session.starttls()
        elif conf['MAIL_SSL']:
            self.session = smtplib.SMTP_SSL(host=conf['MAIL_SERVER'], port=conf['MAIL_PORT'])
        else:
            self.session = smtplib.SMTP(host=conf['MAIL_SERVER'], port=conf['MAIL_PORT'])
        
        if conf['USE_CREDENTIALS']:
            self.session.login(conf['MAIL_USERNAME'], conf['MAIL_PASSWORD'])

    def send_message(self, message):
        msg = MIMEMultipart()
        msg['From'] = MAIL_FROM
        msg['Subject'] = message['subject']
        msg.attach(MIMEText(message['body'], message.get('mimetype', 'plain')))

        for recipient in message.get('recipients', []):
            msg['To'] = recipient
            self.session.send_message(msg)


class Mailer:
    def __init__(self):
        self.conf = {
            "MAIL_USERNAME": MAIL_USERNAME,
            "MAIL_PASSWORD": MAIL_PASSWORD,
            "MAIL_FROM": MAIL_FROM,
            "MAIL_PORT": MAIL_PORT,
            "MAIL_SERVER": MAIL_SERVER,
            "MAIL_TLS": MAIL_TLS,
            "MAIL_SSL": MAIL_SSL,
            "USE_CREDENTIALS": USE_CREDENTIALS
        }

        self.sender = MailSender(self.conf)

        self.message = """
        <h3>Grazie per esserti registrato alla newsletter di Tamatara!</h3>
        <p>A breve saremo online, ti contatteremo solo per offrirti sconti e anticipazioni per ripagare la tua fiducia.</p>
        """

    def send(self, email: str):
        message = {
            'subject': "Registrazione alla Newsletter di Tamatara",
            'recipients': [email],
            'body': self.message,
            'mimetype': 'html'
        }
        self.sender.send_message(message)
        print(f"Email sent to {email}")
