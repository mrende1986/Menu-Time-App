from menutime import mail, app
from flask_mail import Mail, Message
from threading import Thread


def send_email(app, msg):
    with app.app_context():
        mail.send(msg)

def email_new_registration(email_address):
    msg = Message()
    msg.subject = "Menu Time Registration Complete"
    msg.recipients = [email_address]
    msg.sender = 'menutimeapp@gmail.com'
    msg.body = 'Thank you for registering with MenuTime.'
    Thread(target=send_email, args=(app, msg)).start()