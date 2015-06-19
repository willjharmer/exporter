from flask.ext.script import Server, Shell, Manager
from app import AppFactory
from app.configs import Dev

manager = Manager( AppFactory.create(config=Dev))

if __name__ == '__main__':
    manager.run()
