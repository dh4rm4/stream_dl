from flask import render_template, redirect
from app import app
from app.options import dlOptions

@app.route('/', methods=['GET', 'POST'])
@app.route('/stream_dl', methods=['GET', 'POST'])
def main_page():
    form = dlOptions()
    if form.validate_on_submit():
        return form.videoUrl.data
    return render_template('main_page.html', title='Stream DL', form=form)
