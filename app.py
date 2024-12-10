import os
from flask import Flask, render_template, request, g, flash, abort, url_for
from ENIGMA import Cipher as cipher_msg, Decipher as decipher_msg


DEBUG = True
SECRET_KEY = 'IDFKAiddqd123!@%'

app = Flask(__name__)

app.config.from_object(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/process", methods=["POST"])
def process():
    message = request.form['message']
    rotor_order = request.form['rotor_order']
    rotor1 = int(request.form['rotor1'])
    rotor2 = int(request.form['rotor2'])
    rotor3 = int(request.form['rotor3'])
    plugboard = request.form['plugboard']
    
    action = request.form['action']
    
    if action == 'encrypt':
        cipher = cipher_msg(message, rotor_order, rotor1, rotor2, rotor3, plugboard)
        flash(f'Зашифрованное сообщение: {cipher}')
    elif action == 'decrypt':
        decipher = decipher_msg(message, rotor_order, rotor1, rotor2, rotor3, plugboard)
        flash(f'Дешифрованное сообщение: {decipher}')

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)