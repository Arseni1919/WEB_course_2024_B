from flask import Flask, redirect, url_for
from flask import render_template


app = Flask(__name__)


@app.route('/')
@app.route('/home')
def hello_world():
    # DB
    name = 'Ron'
    # name = ''
    user_info = {'firstName': 'Yossi', 'lastName': 'Katz'}
    hobbies = ['tenis', 'swimming', 'programming']
    degrees = ('B.Sc.', 'M.Sc.')
    # redcolor = True
    redcolor = False
    return render_template(
        'index.html',
        name=name,
        user_info=user_info,
        hobbies=hobbies,
        degrees=degrees,
        redcolor=redcolor
    )


@app.route('/d')
@app.route('/default')
@app.route('/default_page')
def default_page():
    return 'Welcome to default Page!'


@app.route('/about', methods=['GET', 'PUT', 'POST', 'DELETE'])
def about_page():
    # return redirect('/default')
    # return redirect(url_for('default_page'))
    return render_template('about.html')


app.run(debug=True, port=5001)
