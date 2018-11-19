import json
from flask import Flask, request, jsonify

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database import Base, User, Item

# declare constants
HOST = '0.0.0.0'
PORT = 5000

# connect to database
engine = create_engine('sqlite:///sample.db')
Base.metadata.bind = engine
# create database session
DBSession = sessionmaker(bind=engine)
session = DBSession()

# initialize flask application
app = Flask(__name__)


# sample hello world page
@app.route('/')
def hello():
    return "<h1>Hello World</h1>"


# sample api endpoint to get all users
@app.route('/api/users')
def get_users():
    users = session.query(User).all()
    return jsonify(status=200, users=[i.serialize for i in users])


# sample api endpoint for items
@app.route('/api/users/<int:user_id>/items', methods=['GET', 'POST'])
def get_items(user_id):
    if request.method == 'POST':
        # get data from post request
        data = request.get_json()
        if data.keys() >= {'name', 'description'}:
            # create new item
            new_item = Item(user_id=user_id,
                            name=data['name'],
                            description=data['description'])
            session.add(new_item)
            session.commit()
            # return success status and new item
            return jsonify(status=201, item=new_item.serialize)
        else:
            # return error status
            return jsonify(status=400)
    else:
        # get all items for user
        items = session.query(Item).filter_by(user_id=user_id).all()
        return jsonify(status=200, items=[i.serialize for i in items])


if __name__ == '__main__':
    app.run(host=HOST,
            debug=True,
            port=PORT)
