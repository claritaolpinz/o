from flask import Flask
from flask_mail import Mail


from office.main.routes import page_not_found
from office.main.routes import internal_error

app = Flask(__name__, static_folder='./static')
app.secret_key = "edeacda59ac156398eb419c6b1ba496a5b8d0250cbf6f09299"
app.register_error_handler(404, page_not_found)
app.register_error_handler(500, internal_error)


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = '' #Gmail here
app.config['MAIL_PASSWORD'] = '' #Gmail app password here


mail = Mail(app)
from office.main.routes import main
from office.portals.routes import portals

app.register_blueprint(main)
app.register_blueprint(portals)