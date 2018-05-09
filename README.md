# STREAM_DL

Stream_dl is a docker image "Ready to use", to dowload contents from a large majority of streaming platforms.
The tech used are as below:
* [Python 3.5](https://www.python.org/)
* [Youtube-dl](https://rg3.github.io/youtube-dl/supportedsites.html)
* [Flask](http://flask.pocoo.org/)
* [Nginx](https://www.nginx.com/)
* [Gunicorn](http://gunicorn.org/)

![](https://raw.githubusercontent.com/dh4rm4/stream_dl/master/src/app/static/img/stream_dl_overview.png)


## Installation

OS X & Linux:

```
You must install docker and its dependancies.
```

```sh
$ git clone https://github.com/dh4rm4/stream_dl &&
$ cd stream_dl
$ sudo docker build . -t stream_dl:latest 
```

## Usage example

```sh
$ sudo docker run -p 5000:5000 stream_dl:latest
```
