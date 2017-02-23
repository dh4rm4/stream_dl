# STREAM_DL

Stream_dl is a userfriendly interface to download/convert stream videos

## Installing

### Automatically
```
sudo python2 checkDependancies
```

### Manually
First you need to install pip
```
sudo apt-get install python-pip
```
Also a specific library
```
sudo apt-get install libav-tools
```
And finally all those python(2) modules via pip
```
sudo pip install [module_name]
```
```
tkinter
ttk
PIL
youtube-dl
```

### Built With

* [youtube-dl](https://github.com/rg3/youtube-dl) : the module to download video
* [tkinter](https://docs.python.org/2/library/tkinter.html) : the graphical module

### Error
If you have the error ""ValueError: unknown url type: /yts/jsbin/player-en_US-vflV3n15C/base.js", you can solve it with this method:
* [Fix #11892](https://github.com/rg3/youtube-dl/pull/11892/files) : a fix form * [Khang-NT](https://github.com/Khang-NT)