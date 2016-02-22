from flask import Flask
from flask import render_template
from flask_mail import Mail
from flask_mail import Message
from flaskext.mysql import MySQL
from itsdangerous import URLSafeTimedSerializer
from passwords import conf

app = Flask(__name__)
# uncomment to turn on debugging
#app.config['DEBUG'] = True

app.config.update(
  # EMAIL SETTINGS
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 465,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = conf.email_user,
    MAIL_PASSWORD = conf.email_pass,
  # MySQL configurations
    MYSQL_DATABASE_USER = 'root',
    MYSQL_DATABASE_PASSWORD = conf.sql_pass,
    MYSQL_DATABASE_DB = 'uwevents',
    MYSQL_DATABASE_HOST = 'localhost',
  # Secret Passwords!
    SECRET_KEY = 'password1',
    SECURITY_PASSWORD_SALT = 'password2'
    )

mail = Mail(app)
mysql = MySQL()
mysql.init_app(app)


def send_email(to, subject, template):
    msg = Message(
                subject,
                recipients=[to],
                html=template,
                sender="notify@uwevents.gq")
    mail.send(msg)

def send_bulk_email(subList, yourevents, homepage):
    with mail.connect() as conn:
        
        subject = "This Week's Events"
        for user in subList:
            if user[3] == 1:
                yourname = user[1]
                youremail = user[2]
                with app.app_context():
                    template = render_template('event-notify.html',
                                        name=yourname,
                                        events=yourevents,
                                        home=homepage)
                    msg = Message(
                                subject,
                                recipients=[youremail],
                                html=template,
                                sender="notify@uwevents.gq")
                    conn.send(msg)

key = URLSafeTimedSerializer(app.config["SECRET_KEY"])
