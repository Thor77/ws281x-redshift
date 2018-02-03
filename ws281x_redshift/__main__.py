from datetime import datetime, time
from time import sleep

from ws281x_redshift.redshift import calculate_color
from ws281x_redshift.strip import initialize_strip


def main():
    sunrise = time(8)
    sunset = time(17, 30)
    # initialize strip
    strip = initialize_strip()
    while True:
        # set strip to current color
        current_color = calculate_color(datetime.now().time(), sunrise, sunset)
        for i in range(strip.numPixels()):
            strip.setPixelColorRGB(
                i, int(current_color.r),
                int(current_color.g), int(current_color.b)
            )
        strip.show()
        sleep(0.1)


if __name__ == '__main__':
    main()
