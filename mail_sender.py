from flask import Flask, request, render_template, json
import re
import os.path

from flask_admin.contrib.fileadmin import FileAdmin
from flask_admin import Admin
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)

app.config.from_object('config')

# Create administrative view using flask-admin.
admin = Admin(app, template_mode="bootstrap3")

path = os.path.join(os.path.dirname(__file__), 'static')
admin.add_view(FileAdmin(path, '/static/assets/img/', name='Pliki Statyczne'))

app.config['SECRET_KEY']
# Mail server configuration.
app.config['MAIL_SERVER']
app.config['MAIL_PORT']
app.config['MAIL_USERNAME']
app.config['MAIL_PASSWORD']
app.config['MAIL_USE_TLS']
app.config['MAIL_USE_SSL']
mail = Mail(app)


@app.route('/')
def index():
    """Display the homepage"""
    return render_template('index.html')


@app.route('/mail_sender', methods=['POST'])
def process():
    """User input data validation and sending an e-mail"""

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

    # Send an e-mail, if data is valid:
    msg = Message("wiadomość z formularza", sender=app.config['MAIL_USERNAME'], recipients=["wiyerid@poly-swarm.com"])
    msg.body = "od {}, ({}) , wiadomosc:--->{}  ".format(name, email, user_message)
    mail.send(msg)
    # Returning json success message to jquery:
    return json.dumps({"success": "Twoja wiadomość została wysłana!"})


if __name__ == '__main__':
    app.run(debug=True)
