from flask import Flask, render_template, request, redirect, url_for, flash
import os

SECRET_KEY = os.urandom(32)

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        agents_count = request.form.get('agents')
        objects_count = request.form.get('objects')
        if not request.form['agents'] or not request.form['objects']:
            flash('Please fill all fields', 'error')
        elif int(agents_count) < 1 or int(objects_count) < 1:
            flash('Agents and objects must be larger or equal to 1', 'error')
        else:
            return redirect(url_for('allocation',
                                    agents_count=int(agents_count),
                                    objects_count=int(objects_count)))
    return render_template('index.html')


@app.route('/allocation/<agents_count>/<objects_count>', methods=['GET', 'POST'])
def allocation(agents_count, objects_count):
    if request.method == 'POST':
        user_input = request.form.getlist('ag_input')
        user_input = ','.join(user_input)
        return redirect(url_for('calculation',
                                agents_count=int(agents_count),
                                objects_count=int(objects_count),
                                user_input=user_input))
    return render_template('allocation.html', agents=int(agents_count), objects=int(objects_count))


@app.route('/calculation/<agents_count>/<objects_count>/<user_input>')
def calculation(agents_count, objects_count, user_input):
    return render_template('calculation.html',
                           agents=int(agents_count),
                           objects=int(objects_count),
                           input=user_input)


if __name__ == "__main__":
    app.run(debug=True)
