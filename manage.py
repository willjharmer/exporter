from flask.ext.script import Manager
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate, MigrateCommand
from app import AppFactory
from app.configs import Dev

app = AppFactory.create(config=Dev)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

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



