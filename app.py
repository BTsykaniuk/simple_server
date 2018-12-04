from flask import Flask
from flask_mongoengine import MongoEngine
import models


app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "projectdb"}

db = MongoEngine(app)


def register_blueprints():
    # Prevents circular imports
    from view import users
    app.register_blueprint(users)


register_blueprints()


if __name__ == '__main__':
    app.run()
