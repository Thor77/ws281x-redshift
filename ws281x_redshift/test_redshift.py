from datetime import time

import pytest

from ws281x_redshift.redshift import (RedshiftColor, calculate_color,
                                      calculate_percentages)

sunrise = time(8)
sunset = time(17, 30)


@pytest.mark.parametrize('input_dt,expected', [
    (time(8), (0, 1)), (time(9), (0.11, 0.89)), (time(10), (0.21, 0.79)),
    (time(16), (0.84, 0.16)), (time(17), (0.95, 0.05)), (time(18), (0, 1))
])
def test_calculate_percentages(input_dt, expected):
    assert calculate_percentages(input_dt, sunrise, sunset) == expected


@pytest.mark.parametrize('color,factor,expected', [
    (RedshiftColor(255, 255, 255), 0.5, RedshiftColor(127.5, 127.5, 127.5)),
    (RedshiftColor(127.5, 127.5, 127.5), 2, RedshiftColor(255, 255, 255)),
    (RedshiftColor(1, 1, 1), 5, RedshiftColor(5, 5, 5))
])
def test_color_multiplication(color, factor, expected):
    assert color * factor == expected


@pytest.mark.parametrize('color1,color2,expected', [
    (RedshiftColor(1, 1, 1), RedshiftColor(1, 1, 1), RedshiftColor(2, 2, 2)),
    (
        RedshiftColor(100, 100, 100), RedshiftColor(100, 100, 100),
        RedshiftColor(200, 200, 200)
    )
])
def test_color_add(color1, color2, expected):
    assert color1 + color2 == expected


@pytest.mark.parametrize('current,expected', [
    (time(17, 20), RedshiftColor(250, 0, 5))
])
def test_calculate_color(current, expected):
    assert calculate_color(current, sunrise, sunset) == expected
