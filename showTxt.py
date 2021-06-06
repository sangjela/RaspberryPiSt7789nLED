# original = https://www.mikan-tech.net/entry/raspi-st7789-lcd
import ST7789
from PIL import Image, ImageDraw, ImageFont

# Create a display instance
disp = ST7789.ST7789(port=0, cs=0, rst=5, dc=6, backlight=13, spi_speed_hz=80 * 1000 * 1000)

# Added: Change to SPI MODE 3
disp._spi.mode = 3
disp.reset()
disp._init()

# Define fonts
# for font $ sudo apt install fonts-noto-cjk fonts-roboto
FONT_ROBOTO = ImageFont.truetype("Roboto-Medium.ttf", 24)
FONT_NOTO = ImageFont.truetype("NotoSansCJK-Regular.ttc", 48)
FONT_NOTO_SMALL = ImageFont.truetype("NotoSansCJK-Regular.ttc", 24)

# Define colors
COLOR_ORANGE = (255, 167, 38)
COLOR_GREEN = (129, 199, 132)
COLOR_LIGHT_BLUE = (129, 129, 255)

# Create an image with black background
image = Image.new("RGB", (disp.width, disp.height), (0, 0, 0))

# Draw some text
draw = ImageDraw.Draw(image)
draw.text((0, 0), "일본백수", font=FONT_NOTO, fill=COLOR_ORANGE)
draw.text((48, 48), "이제부터", font=FONT_NOTO, fill=COLOR_ORANGE)
draw.text((0, 96), "뭐먹고사나", font=FONT_NOTO, fill=COLOR_ORANGE)
draw.text((0, 160), "내인생은어디로간다냐~", font=FONT_NOTO_SMALL, fill=COLOR_GREEN)
draw.text((0, 200), "abcedfghijklmnopqr", font=FONT_ROBOTO, fill=COLOR_LIGHT_BLUE)


# Show it on display
disp.display(image)