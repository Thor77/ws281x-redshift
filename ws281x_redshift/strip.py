from neopixel import Adafruit_NeoPixel, ws

# LED strip configuration:
LED_COUNT = 60
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 255
LED_INVERT = False
LED_CHANNEL = 0
LED_STRIP = ws.WS2811_STRIP_GRB


def initialize_strip():
    strip = Adafruit_NeoPixel(
        LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA,
        LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP
    )
    strip.begin()
    return strip
