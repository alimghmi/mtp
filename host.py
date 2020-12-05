import random
import time
import string
from flask import Flask, render_template, session, url_for, redirect, request
import logging

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)
app.secret_key = b'547785_5#y2L"F4Q8z\n\xec]/kW4^ja5ef'

@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('main'))

@app.route('/redirect')
def rdrct():
    if 'csrf' in session:
        time.sleep(1)
        return redirect(session['csrf'])

    return redirect('tg://resolve/?domain=imtproto')

@app.route('/')
def main():
    server = request.args.get("q")
    if server != None:
    	proxy = f'tg://proxy?server={server}&port=443&secret=ee42aad8aa14b76f7bd88d381eeb5a896f6f6e652e6f6e652e6f6e652e6f6e65'
    	return redirect(proxy)

    return '<code>Powered by arvancloud</code>'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
