from flask import Flask, redirect, url_for
from flask import render_template
from flask import request, session


app = Flask(__name__)
app.secret_key = '123'


@app.route('/')
@app.route('/home')
def index():
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


@app.route('/logout')
def logout_func():
    del session['username']
    del session['email']
    session['logged_in'] = False
    return redirect(url_for('login_func'))


# @app.route('/login', methods=['GET'])
@app.route('/login', methods=['GET', 'POST'])
def login_func():
    req_method = request.method
    if req_method == 'GET':
        session['logged_in'] = False
        return render_template(
            'login.html',
            req_method=req_method
        )
    if req_method == 'POST':
        username = request.form['username']
        email = request.form['email']
        # DB check
        session['username'] = username
        session['email'] = email
        session['logged_in'] = True
        return render_template(
            'login.html',
            req_method=req_method,
            username=username,
            email=email,
        )

    # return redirect(url_for('index'))


# @app.route('/')
# def main_page():
#     if 'username' in session:
#         username = session.get('username')
#         email = session.get('email')
#         return render_template('lecture7_flask.html',
#                                name=username,
#                                second_name=email,
#                                hobbies=['Art', 'Sports', 'Computers', 'Programming', 'AI', 'Youtube'],
#                                user_details={'id': 123, 'color': 'orange', 'height': 100}
#                                )
#     return render_template('lecture7_flask.html',
#                            hobbies=['Art', 'Sports', 'Computers', 'Programming', 'AI', 'Youtube'],
#                            user_details={'id': 123, 'color': 'orange', 'height': 100}
#                            )
#
#
# @app.route('/profile', methods=['GET', 'POST', 'PUT'])
# def profile_page():
#     # do something with DB for example
#     # return redirect('/')
#     return redirect(url_for('hello_world'))
#
#
# @app.route('/about', methods=['GET'])
# @app.route('/about/me')
# def about_page():
#     return render_template('about.html')
#
#
# @app.route('/users', defaults={'user_id': 123})
# @app.route('/users/<int:user_id>')
# def users_id_func(user_id):
#     # DB ...
#     return render_template('users.html', user_id=user_id)
#
#
# @app.route('/<category>/<int:cat_id>/<subcategory>/name')
# def foo_func(category, cat_id, subcategory):
#     return f'{category=}, {cat_id=}, {subcategory=}'
#
#
# @app.route('/api/users/<int:user_id>')
# def api_users(user_id):
#     # DB ...
#     # user_data = {
#     #     'name': 'Dana',
#     #     'id': user_id,
#     #     'hobby': 'computers'
#     # }
#     user_data = OrderedDict()
#     user_data['name'] = 'Dana'
#     user_data['id'] = user_id
#     user_data['hobby'] = 'computers'
#
#     for k, v in user_data.items():
#         print(f'{k}: {v}')
#
#     return jsonify(user_data)
#
#
# @app.route('/logout', methods=['GET'])
# def logout_func():
#     session['logged_in'] = False
#     session['username'] = ''
#     session['email'] = ''
#     return redirect(url_for('login_func'))
#
#
# @app.route('/login', methods=['GET', 'POST'])
# def login_func():
#     print(f'The method is: {request.method}')
#     if request.method == 'POST':
#         if 'username' in request.form:
#             username = request.form['username']
#             email = request.form['email']
#             password = request.form['password']
#             # check the password with DB
#             session['username'] = username
#             session['email'] = email
#             session['logged_in'] = True
#             return render_template('login.html',
#                                    post_username=username, post_email=email)
#         return render_template('login.html')
#     if request.method == 'GET':
#         if 'username' in request.args:
#             username = request.args['username']
#             email = request.args['email']
#             password = request.args['password']
#             # check the password with DB
#             session['username'] = username
#             session['email'] = email
#             return render_template('login.html',
#                                    username=username, email=email)
#         return render_template('login.html')


app.run(debug=True, port=5001)
