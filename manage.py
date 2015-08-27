from flask.ext.script import Manager
from app import AppFactory
from app.configs import Dev

app = AppFactory.create(config=Dev)

manager = Manager(app)

if __name__ == '__main__':
    manager.run()
