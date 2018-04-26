from flask import render_template
from app import app

@app.route('/')
@app.route('/stream_dl')
def main_page():
    return render_template('main_page.html', title='Stream DL')
