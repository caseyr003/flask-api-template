# Flask API Template

This project is a flask api built with Python, Flask and SQLAlchemy to be used as a starter template.

## Built With

* [Python 3](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)
* [Docker](https://www.docker.com/)
* [SQLAlchemy](https://www.sqlalchemy.org/)

## Prerequisites

You will need the following things properly installed on your computer:

* [Git](http://git-scm.com/)
* [Python 3](https://www.python.org/)
* [Docker](https://www.docker.com/)

## Installation

* run `git clone https://github.com/caseyr003/flask-api-template.git`

## Running

To run the project locally follow the following steps:

* change into the project directory
* `docker build -t backend-api .`
* `docker run -p 5000:5000 --name api backend-api`

## JSON API

The JSON API has sample endpoints to start development

* `http://localhost:5000/`
(returns hello world html)

* `http://localhost:5000/api/users`
(returns all users in database)

* `http://localhost:5000/api/user/<user_id>/items`
(returns all items for users)


## License

This project is licensed under the MIT License
