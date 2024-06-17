import json
from pprint import pprint
from flask import Flask, redirect, url_for
from flask import render_template
from flask import request, session


app = Flask(__name__)
app.secret_key = '123'


# ------------------------------------------------------------------ #
# ------------------------------------------------------------------ #
# ------------------------------------------------------------------ #
# FLASK
# ------------------------------------------------------------------ #
# ------------------------------------------------------------------ #
# ------------------------------------------------------------------ #

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


# ------------------------------------------------------------------ #
# ------------------------------------------------------------------ #
# ------------------------------------------------------------------ #
# MONGODB
# ------------------------------------------------------------------ #
# ------------------------------------------------------------------ #
# ------------------------------------------------------------------ #
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://1919ars:1919ars@cluster0.kg52uoz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new cluster and connect to the server
cluster = MongoClient(uri, server_api=ServerApi('1'))
mydatabase = cluster['mydatabase']
customers_col = mydatabase['customers']

# sample_analytics_db = cluster['sample_analytics']


@app.route('/mongodb')
def mongodb_func():
    # message = 'good'
    # message = pymongo.version
    # sample_analytics_db = cluster['sample_analytics']
    # message = sample_analytics_db.list_collection_names()
    # message = cluster.list_database_names()
    # message = mydatabase.list_collection_names()

    # insert_one
    # my_dict = {
    #     'name': 'John',
    #     'address': 'Highway 37',
    #     'rating': 10
    # }
    # customers_col.insert_one(my_dict)
    # # message = cluster.list_database_names()
    # message = mydatabase.list_collection_names()

    # insert_many
    # my_list = [
    #     {'name': 'Tal', 'address': 'Hogwards 37', 'rating': 11},
    #     {'name': 'Bekka', 'address': 'Bronx 3', 'rating': 20},
    #     {'name': 'Alisa', 'address': 'Area 9', 'rating': 30},
    # ]
    # customers_col.insert_many(my_list)
    # message = mydatabase.list_collection_names()

    # find
    # my_list = list(customers_col.find())

    # find query
    # myquery = {'name': 'John'}
    # my_list = list(customers_col.find(myquery))

    # myquery = {'rating': {"$gt": 10}}
    # my_list = list(customers_col.find(myquery))

    # sort
    # my_list = list(customers_col.find().sort('name'))
    # my_list = list(customers_col.find().sort('name', -1))

    # limit
    # message = len(list(customers_col.find()))
    # my_list = list(customers_col.find().limit(3))
    # my_list = list(customers_col.find().sort('rating', -1).limit(3))

    # findOne
    # message = customers_col.find_one({'name': 'John'})

    # update one
    # my_query = {'address': 'Highway 37'}
    # new_values = {'$set': {'address': 'Canyon 123'}}
    # customers_col.update_one(my_query, new_values)
    # my_list = list(customers_col.find())

    # update many
    # customers_col.update_many({}, {'$inc': {'rating': 1}})
    # customers_col.update_many({}, {'$set': {'rating': 1}})
    # my_list = list(customers_col.find())

    # delete one
    # customers_col.delete_one({'name': 'Alisa'})
    # my_list = list(customers_col.find())

    # delete many
    # customers_col.delete_many({'rating': {'$gt': 0}})
    # my_list = list(customers_col.find())

    # aggregations
    # aggregation = [
    #     {
    #         '$match': {
    #             'rating': {
    #                 '$gt': 0
    #             }
    #         }
    #     }, {
    #         '$sort': {
    #             'rating': 1
    #         }
    #     }, {
    #         '$limit': 2
    #     }
    # ]
    # my_list = list(customers_col.aggregate(aggregation))

    my_list = customers_col.find()
    # return render_template('mongodb_lecture.html', message=message)
    return render_template('mongodb_lecture.html', my_list=my_list)


@app.route('/db_insert')
def insert_func():
    # insert_one
    my_dict = {
        'name': request.args['name'],
        'address': request.args['address'],
        'rating': int(request.args['rating']),
    }
    customers_col.insert_one(my_dict)
    return redirect(url_for('mongodb_func'))


@app.route('/db_delete', methods=['POST'])
def delete_func():
    print(request.form)
    customers_col.delete_one({'name': request.form['name']})
    return redirect(url_for('mongodb_func'))


@app.route('/db_increment')
def increment_func():
    customers_col.update_many({}, {'$inc': {'rating': 1}})
    return redirect(url_for('mongodb_func'))


# ------------------------------------------------------------------ #
# ------------------------------------------------------------------ #
# ------------------------------------------------------------------ #
# FETCH
# ------------------------------------------------------------------ #
# ------------------------------------------------------------------ #
# ------------------------------------------------------------------ #

@app.route('/fetch_page')
def fetch_page_func():
    return render_template('fetch_example.html')


@app.route('/fetch_example', methods=['GET', 'POST'])
def fetch_example_func():
    if request.method == 'GET':
        data = {'message': 'GET response'}
        return json.dumps(data)
    if request.method == 'POST':
        mydict = request.json
        print(type(mydict))
        data = {'message': 'POST response'}
        data.update(mydict)
        return json.dumps(data)
    raise RuntimeError('no no')


# ------------------------------------------------------------------ #
# ------------------------------------------------------------------ #
# ------------------------------------------------------------------ #
app.run(debug=True, port=5000)

