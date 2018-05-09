from flask import render_template, redirect, send_from_directory, make_response, request
from app import app
from app.options import dlOptions
from app.streamDlCore import streamDlCore
import os

@app.route('/', methods=['GET', 'POST'])
@app.route('/stream_dl', methods=['GET', 'POST'])
def main_page():
    form = dlOptions()
    if form.validate_on_submit():
        cur_session = streamDlCore(form.videoUrl.data,
                                   form.quality_list.data,
                                   form.format_list.data,
                                   form.dl_playlist.data)
        cur_session.start()
        archive_path = cur_session.get_path()
        return render_template('dl_page.html',
                               title = 'Download Page',
                               archive_path = archive_path)
    return render_template('main_page.html', title='Stream DL', form=form)


@app.route('/stream_dl/dl_archive', methods=['GET'])
def download_page():
    filename = request.values['archive_path']
    return send_from_directory('dl', filename)


@app.errorhandler(404)
def handle_bad_request(error):
        return render_template('404.html')

    
@app.errorhandler(500)
def handle_bad_request(error):
        return render_template('500.html')
