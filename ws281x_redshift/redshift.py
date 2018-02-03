from datetime import timedelta


class RedshiftColor(object):
    def __init__(self, r, g, b):
        self.r, self.g, self.b = r, g, b

    def __add__(self, other):
        return RedshiftColor(
            self.r + other.r, self.g + other.g, self.b + other.b
        )

    def __iadd__(self, other):
        self.r += other.r
        self.g += other.g
        self.b += other.b
        return self

    def __mul__(self, factor):
        return RedshiftColor(
            round(self.r * factor),
            round(self.g * factor),
            round(self.b * factor)
        )

    def __imul__(self, factor):
        self.r = round(self.r * factor)
        self.g = round(self.g * factor)
        self.b = round(self.b * factor)
        return self

    def __eq__(self, other):
        return self.r == other.r and self.g == other.r and self.b == other.b

    def __repr__(self):
        return 'RedshiftColor(r={}, g={}, b={})'.format(self.r, self.g, self.b)

    def __str__(self):
        return '({}, {}, {})'.format(self.r, self.g, self.b)


def difference(t1, t2):
    '''
    Calculate difference between two times

    :type t1: datetime.time
    :type t2: datetime.time

    :return: t1 - t2
    :rtype: datetime.timedelta
    '''
    return timedelta(
        hours=t1.hour - t2.hour,
        minutes=t1.minute - t2.minute,
        seconds=t1.second - t2.second,
        microseconds=t1.microsecond - t2.microsecond
    )


def mix_percent(color1, color2, percent):
    '''
    Calculate a mix of two colors, using `percent` of each other

    :param color1: First color
    :param color2: Second color
    :param percent: Percent used of color2 for mixing

    :type color1: neopixel.Color
    :type color2: neopixel.Color
    :type percent: int

    :return: Resulting mixed color
    :rtype: neopixel.Color
    '''
    pass


def calculate_percentages(current, sunrise, sunset):
    '''
    Calculate current percentage of day/night from current

    :param current: Current time
    :param sunrise: Sunrise time
    :param sunset: Sunset time

    :type current: datetime.time
    :type sunrise: datetime.time
    :type sunset: datetime.time

    :return: (day percentage, night percentage)
    :rtype: tuple
    '''
    if current <= sunrise or current >= sunset:
        # return night color if current is before sunrise or after sunset
        return 0, 1
    # calculate difference between current time and sunrise/sunset
    sunrise_distance = difference(current, sunrise).total_seconds()
    sunset_distance = difference(sunset, current).total_seconds()
    sunset_sunrise_distance = difference(sunset, sunrise).total_seconds()
    # calculate percentage of day and night
    day_percent = round(sunset_distance / sunset_sunrise_distance, 2)
    night_percent = round(sunrise_distance / sunset_sunrise_distance, 2)
    return day_percent, night_percent


def calculate_color(current, sunrise, sunset):
    '''
    Calculate color for a specific datetime

    :param current: Current time
    :type current: datetime.time

    :param sunrise: Time of sunrise
    :type sunrise: datetime.time

    :param sunset: Time of sunset
    :type sunset: datetime.time

    :return: Color for current time
    :rtype: neopixel.Color
    '''
    day_color = RedshiftColor(0, 0, 255)
    night_color = RedshiftColor(255, 0, 0)
    day_pc, night_pc = calculate_percentages(current, sunrise, sunset)
    day_color_pc = day_color * day_pc
    night_color_pc = night_color * night_pc
    return day_color_pc + night_color_pc
