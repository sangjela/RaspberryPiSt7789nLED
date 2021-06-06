# original = https://www.mikan-tech.net/entry/raspi-st7789-lcd
import ST7789
from PIL import Image

# Create a display instance
disp = ST7789.ST7789(port=0, cs=0, rst=5, dc=6, backlight=13, spi_speed_hz=80 * 1000 * 1000)

# Added: Change to SPI MODE 3
disp._spi.mode = 3
disp.reset()
disp._init()

# Create a green image
image = Image.new("RGB", (disp.width, disp.height), (67, 160, 71))

# Show it on display
disp.display(image)