from flask import render_template, redirect
from app import app
from app.options import dlOptions
#from app.streamDlCore import streamDlCore


class get_user_options(object):
    """
    adapt options fetch from website
    """

    def __init__(self, form_vUrl, form_quality, form_formats, form_dl_playlist):
        self.vUrl = self.getUrl(form_vUrl)
        self.quality = self.getQuality(form_quality)
        self.formats = self.getFormats(form_formats)
        self.dl_playlist = self.getDlPlaylist(form_dl_playlist)

    def

@app.route('/', methods=['GET', 'POST'])
@app.route('/stream_dl', methods=['GET', 'POST'])
def main_page():
    form = dlOptions()
    if form.validate_on_submit():
#        cur_session = streamDlCore(form.videoUrl.data,
#                                     form.quality_list.data,
#                                     form.format_list.data,
#                                     form.dl_playlist.data)
#        cur_session.start()
#        archive_path = cur_session.get_path()
        for boid in form.quality_list.choices:
            if boid[0] == form.quality_list.data:
                print (boid)
        return form.quality_list.data
    return render_template('main_page.html', title='Stream DL', form=form)
