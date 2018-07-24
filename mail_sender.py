from flask import Flask, request, render_template, json

from flask_mail import Mail, Message


app = Flask(__name__)
mail = Mail(app)

app.secret_key = "development key"

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'mail@gmail.com'
app.config['MAIL_PASSWORD'] = "some password"
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/mail_sender', methods=['POST'])
def process():
    email = request.form['email']
    name = request.form['name']
    user_message = request.form['message']

    msg = Message("wiadomość z formularza", sender="mail@gmail.com", recipients=["recipient@gmail.com"])
    msg.body = "od {}, ({}) , wiadomość:--->  " .format(name, email)
    mail.send(msg)
    return json.dumps({"success" : "Your message was sent successfully!"})



if __name__ == '__main__':
    app.run(debug=True)

