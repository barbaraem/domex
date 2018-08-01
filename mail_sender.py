
from flask import Flask, request, render_template, json
import re

from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)

app.secret_key = "development key"

# mail server configuration
app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = "sender@email.com"
app.config['MAIL_PASSWORD'] = "sender_pass"
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route('/')
def index():
    """display the homepage"""
    return render_template('index.html')


@app.route('/mail_sender', methods=['POST'])
def process():
    """user input data validation and sending an e-mail"""

    email = request.form['email']
    name = request.form['name']
    user_message = request.form['message']

    pattern = r"^[_a-zA-Z0-9-]+(\.[_a-zA-Z0-9-]+)*@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]{1,})*\.([a-zA-Z]{2,}){1}$"

    if not email:
        return json.dumps({"error": {"email": "Podaj swój adres email!"}})

    if re.match(pattern, email) == None:
        print(email)
        return json.dumps({"error": {"email": "Podaj właściwy adres e-mail!"}})

    if not name:
        return json.dumps({"error": {"name": "Wpisz imię!"}})
    if not user_message:
        return json.dumps({"error": {"message": "Wpisz swoją wiadomość!"}})

    # send an e-mail, if data is valid:
    msg = Message("wiadomość z formularza", sender="sender@email.com", recipients=["wiyerid@poly-swarm.com"])
    msg.body = "od {}, ({}) , wiadomosc:--->{}  ".format(name, email, user_message)
    mail.send(msg)
    # returning json success message to jquery:
    return json.dumps({"success": "Twoja wiadomość została wysłana!"})


if __name__ == '__main__':
    app.run(debug=True)
