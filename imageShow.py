# original = https://www.mikan-tech.net/entry/raspi-st7789-lcd
import ST7789
from PIL import Image

from time import sleep

# Create a display instance
disp = ST7789.ST7789(port=0, cs=0, rst=5, dc=6, backlight=13, spi_speed_hz=80 * 1000 * 1000)

# Added: Change to SPI MODE 3
disp._spi.mode = 3
disp.reset()
disp._init()

# Open image file
#image = Image.open("car_omocha_red.jpg")
image = Image.open("knightRider.jpg")



# Resize to screen size
image = image.resize((disp.width, disp.height), resample=Image.LANCZOS)

# Show it on display
disp.display(image)

# for Image # 2 ================================
sleep(5)
#disp._init()

# Open image file
image = Image.open("utaha_240.jpg")

# Show it on display
disp.display(image)

