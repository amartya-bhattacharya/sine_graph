from math import pi

from wtforms import Form, FloatField, validators


# Creates the input fields for the parameters
class InputForm(Form):
    amp = FloatField(
        label='amplitude (m)', default=1.0,
        validators=[validators.InputRequired()])
    freq = FloatField(
        label='frequency (1/s)', default=1 / (2 * pi),
        validators=[validators.InputRequired()])
    x_max = FloatField(
        label='x max (degrees)', default=720,
        validators=[validators.InputRequired()])
