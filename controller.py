from flask import Flask, render_template, request

from compute import compute
from model import InputForm

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    # Gets the form from model.py
    form = InputForm(request.form)
    # Checks for input
    if request.method == 'POST' and form.validate():
        # Creates sine graph given inputs
        result = compute(form.amp.data, form.freq.data, form.x_max.data)
    else:
        result = None
    return render_template('view.html', form=form,
                           result=result)


if __name__ == '__main__':
    app.run(debug=True)
