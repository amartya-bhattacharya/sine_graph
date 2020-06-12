import bokeh.plotting as plt
from bokeh.embed import components
from numpy import pi, sin, radians, linspace


def equation(x, amp, freq):
    # Calculate sin(x) given amp and freq and max x
    return amp * sin(2 * pi * float(freq) * radians(x))


def compute(amp, freq, x_max, resolution=500):
    # define x and y range
    x_values = linspace(0, x_max, resolution + 1)
    y_values = equation(x_values, amp, freq)

    # Create a new plot with a title and axis labels
    graph = plt.figure(title="sine wave", x_axis_label='x (degrees)', y_axis_label='y = sin(x)')

    # Add a line renderer
    graph.line(x_values, y_values)

    # Get HTML components from Bokeh graph
    script, div = components(graph)
    return script, div


if __name__ == '__main__':
    print(compute(1, 1, 20))
