from flask import render_template, redirect, send_file, make_response
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


@app.route('/<archive_path>')
def download_page(archive_path):
    file_size= os.path.getsize('/webapps/stream_dl/src/dl/boid.img')    
    filename = 'boid.img'#archive_path.split('/')[-1]
    response = make_response()
    path_server = '/download/boid'
    response.headers['Content-Description'] = 'File Transfer'
    response.headers['Cache-Control'] = 'no-cache'
    response.headers['Content-Type'] = 'application/octet-stream'
    response.headers['Content-Disposition'] = 'attachment; filename=%s' % filename
    response.headers['Content-Length'] = file_size
    response.headers['X-Accel-Redirect'] = path_server
    return response


@app.errorhandler(404)
def handle_bad_request(error):
        return render_template('404.html')

@app.errorhandler(500)
def handle_bad_request(error):
        return render_template('500.html')

