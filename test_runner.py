from flask.ext.script import Manager, Command
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate, MigrateCommand
from app import AppFactory
from app.configs import Dev
import os

app = AppFactory.create(config=Dev)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

class Tests(Command):
    description = 'Runs Lettuce and Nose tests.'

    def run(self):
        lettuce_options = "--tag=Browser"
        nose_options = "--rednose --force-color"
        os.system('lettuce ' + lettuce_options)
        os.system('nosetests ' + nose_options)

manager.add_command("test", Tests())

class TableA(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    colA = db.Column(db.String(128))
    colB = db.Column(db.String(128))
    colC = db.Column(db.String(128))

class AnotherTableB(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    colA = db.Column(db.String(128))
    colB = db.Column(db.String(128))
    colC = db.Column(db.String(128))

class DatatableC(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    colA = db.Column(db.String(128))
    colB = db.Column(db.String(128))
    colC = db.Column(db.String(128))

if __name__ == '__main__':
    manager.run()



