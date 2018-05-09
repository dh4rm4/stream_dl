from __future__ import unicode_literals
import youtube_dl
import random
import string
import os
import shutil


class myLogger(object):
    """
    youtube-dl logger
    """

    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


class streamDlCore(object):
    """
    Class calling youtube-dl package
    -> download video
    -> convert it
    -> create archive with all converted files
    """

    def __init__(self, url, quality, vFormat, dl_playlist):
        self.url = url
        self.postProcessor = self.get_postProcessor(quality, vFormat)
        self.vFormat = self.get_vFormat(vFormat, quality)
        self.dl_playlist = self.need_dl_playlist(dl_playlist)
        self.dlDir = self.set_dl_dir()

    def clean_dl_dir(self):
        """
        Remove old files from dl directory
        """
        shutil.rmtree('app/dl')
        if not os.path.exists('app/dl'):
            os.makedirs('app/dl')
       
        
    def get_postProcessor(self, quality, vFormat):
        """
        return dict with options for postDownload process
        """
        if quality == 'min':
            q_kbps = '128'
        else:
            q_kbps = '320'
        if vFormat == 'mp3':
            return [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': q_kbps,
            }]
        return []

    def get_vFormat(self, vformat, quality):
        if vformat == 'mp3':
            if quality == 'max':
                return 'bestaudio'
            return 'worstaudio'
        else:
            if quality == 'max':
                return 'bestvideo'
            return 'worstvideo'

    def need_dl_playlist(self, dl_playlist):
        """
        Return boolean for the option: noplaylist
        """
        if dl_playlist == 'yes':
            return False
        return True

    def get_rand_str(self, a, b):
        return ''.join([random.choice(string.ascii_lowercase)
                        for _ in range(random.randint(a, b))])

    def set_dl_dir(self):
        """
        create a tmp directory with random name
        and return its name
        """
        dirName = self.get_rand_str(8, 8)
        dirPath = 'app/dl/' + dirName + '/'
        if not os.path.exists(dirPath):
            os.makedirs(dirPath)
        return dirPath

    def start(self):
        self.clean_dl_dir()
        options = {
            'format': self.vFormat,
            'postprocessors': self.postProcessor,
            'logger': myLogger(),
            'noplaylist': self.dl_playlist,
            'ignoreerrors': True,
            'outtmpl': self.dlDir + '%(title)s.%(ext)s',
        }
        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([self.url])
        self.create_archive_for_dl()


    def create_archive_for_dl(self):
        self.archive_name = 'your_stream_' + self.get_rand_str(4, 6)
        self.archive_path = 'app/dl/' + self.archive_name
        shutil.make_archive(self.archive_path, 'zip', self.dlDir)
        shutil.rmtree(self.dlDir)

    def get_path(self):
        return (self.archive_name + '.zip')
