# original = https://www.mikan-tech.net/entry/raspi-st7789-lcd
# code for waveshare 240x320 LCD module st7789 https://www.waveshare.com/product/displays/lcd-oled/lcd-oled-3/2inch-lcd-module.htm
# not equal to 240x240, must add cs for init cs=0
import ST7789
from PIL import Image

from time import sleep

# Create a display instance
# display spec is 240 x 320. but it have rotation 90 by default. so width and height exchanged and input
disp = ST7789.ST7789(port=0, cs=0, rst=5, dc=6, backlight=13, width=320,
                 height=240, spi_speed_hz=80 * 1000 * 1000)
#maybe cs=0 -> (CE0) =pin24 =gpio8 for Raspberry Pi 4 pin map

# Added: Change to SPI MODE 3
disp._spi.mode = 3
disp.reset()
disp._init()

#print("%s %d x %d" % (disp, disp.width, disp.height), end=" first disp info\n")

# Open image file
image = Image.open("beauty320.jpg")

# Resize to screen size
image = image.resize((disp.width, disp.height), resample=Image.LANCZOS)
#print(image, end=" resized\n")

# Show it on display
disp.display(image)

# if you saw some Error like this, you can avoid error by doing fix...
# File "/home/pi/.local/lib/python3.7/site-packages/ST7789/__init__.py", line xxx, in image_to_data
#     result[..., [0]] = np.add(np.bitwise_and(pb[..., [0]], 0xF8), np.right_shift(pb[..., [1]], 5))
# ValueError: shape mismatch: value array of shape (240,320,1) could not be broadcast to indexing result of shape (1,320,240)
#
# # How to Fix ... in /ST7789/__init__.py
# result = np.zeros((self._width, self._height, 2), dtype=np.uint8)
# to
# result = np.zeros((self.width, self.height, 2), dtype=np.uint8)

# for Image # 2 ================================
#sleep(5)
#disp._init()

# Open image file
#image = Image.open("utaha_240.jpg")

# Show it on display
#disp.display(image)

