# RaspberryPiSt7789nLED
240x240 IPS LCD Display Run with Raspberry Pi. reference https://www.mikan-tech.net/entry/raspi-st7789-lcd
* I use Raspberry Pi 4 Model B 8GB
* LCD ... SPI communication, st7789 driver

## ● normaly I commit this way...
```
% git pull origin main ... (may be there are update on github, so I must pull before push..)
% git add .
% git status
% git commit -m "Add existing files"
% git push -u origin main  
```

## ● if run some .py, normaly you can see this way...
* https://youtu.be/GG_GYbkBK88 

### .py .jpg list
* imageShow.py show image. default is knight rider car
* ledShows1.py 8 LED softly on/off slowly stream
* imageShow320.py waveshare 240x320 lcd image show. some st7789 driver problem exist. if want fix, see comment in source/
* 2inch240x320and1.3inch240x240.jpg success screen shot for 240x240 and 240x320 image output

### if vscode run on Raspberry pi Git extention when push, request keyring, you can refer this.
* https://askubuntu.com/questions/1256345/cant-connect-to-github-with-vs-code --> sudo apt install gnome-keyring
* you can set keyring password

