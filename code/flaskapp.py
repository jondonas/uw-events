from config import app
from config import key
from config import mysql
from config import send_email
from flask import json
from flask import render_template
from flask import request
from flask import url_for

# app = Flask(__name__)
#app.config['DEBUG'] = True


@app.route("/")
def main():
    return render_template('index.html')

# sign-up page
@app.route('/showSignUp')
def showSignUp():
    return render_template('sign-up.html')

@app.route('/signup', methods=['POST'])
def signUp():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        # read the posted values from the UI
        name  = request.form['inputName']
        email = request.form['inputEmail']
        # validate the received values
        if name and email:
            if "'" in email or '"' in email or "(" in email or " )" in email:
                raise Exception
            if ',' in email or ";" in email or "%" in email:
                raise Exception
            if '"' in name or "(" in name or " )" in name:
                raise Exception
            if "'" in name or ";" in name or "%" in name:
                raise Exception
            # checks if user is already registered
            if cursor.execute('SELECT (1) FROM users WHERE email = %s LIMIT 1',
                              (email)):
                return render_template("already-used.html")
            else:
                # sends confirmation email
                token = key.dumps(email, salt='email-confirm-key')
                confirm_url = url_for('confirm_email',
                                      token=token, _external=True)
                subject = "Confirm Your Email"
                html = render_template('email-confirm.html',
                                       confirm_url=confirm_url,
                                       confirm_name=name)
                send_email(email, subject, html)
                #creates user
                cursor.execute('INSERT INTO users (name,email) VALUES (%s,%s)',
                               (name, email))
                conn.commit()
                return render_template('confirmation.html')
        else:
            return json.dumps({'html':
                               '<span>Enter the required fields</span>'})
        cursor.close()
        conn.close()
    except Exception as e:
        print e
        if "not a valid RFC-5321 address" in str(e):
            return render_template('invalid.html')
        else:
            return json.dumps({'error1': str(e)})


@app.route('/confirm/<token>')
def confirm_email(token):
    try:
        email = key.loads(token, salt="email-confirm-key", max_age=172800)
        if "'" in email or '"' in email or "(" in email or " )" in email:
            raise Exception
        if ',' in email or ";" in email or "%" in email:
            raise Exception
    except Exception as e:
        return str(e)
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('SELECT confirmed FROM users WHERE email=%s', (email,))
        data = cursor.fetchall()
    except Exception as e:
        return str(e)
    if str(data[0][0]) == "1":
        return render_template("already-confirmed.html")
    else:
        try:
            cursor.execute("UPDATE users SET confirmed='1' WHERE email=%s",
                           (email,))
            conn.commit()
            return render_template("activated.html")
        except Exception as e:
            return str(e)
    cursor.close()
    conn.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
