import os
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig

MAIL_USER = os.environ.get('MAIL_USER', '')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', '')
MAIL_FROM = os.environ.get('MAIL_FROM', '')
MAIL_PORT = int(os.environ.get('MAIL_PORT', 587))
MAIL_SERVER = os.environ.get('MAIL_SERVER', '')
MAIL_TLS = True if os.environ.get('MAIL_TLS', 'False') == "True" else False
MAIL_SSL = True if os.environ.get('MAIL_SSL', 'False') == "True" else False
USE_CREDENTIALS = True if os.environ.get('USE_CREDENTIALS', 'False') == "True" else False


class Mailer:
    def __init__(self):
        self.conf = ConnectionConfig(
            MAIL_USERNAME=MAIL_USER,
            MAIL_PASSWORD=MAIL_PASSWORD,
            MAIL_FROM=MAIL_FROM,
            MAIL_PORT=MAIL_PORT,
            MAIL_SERVER=MAIL_SERVER,
            MAIL_TLS=MAIL_TLS,
            MAIL_SSL=MAIL_SSL,
            USE_CREDENTIALS=USE_CREDENTIALS,
        )

        self.template = """
        <h3>Grazie per esserti registrato alla newsletter di Tamatara!</h3>
        <p>A breve saremo online, ti contatteremo solo per offrirti sconti e anticipazioni per ripagare la tua fiducia.</p>
        """

    async def simple_send(self, email: str):
        message = MessageSchema(
            subject="Registrazione alla Newsletter di Tamatara",
            recipients=[email],
            body=template,
            subtype="html",
        )

        fm = FastMail(conf)
        await fm.send_message(message)
        print(f"Email sent to {email}")
