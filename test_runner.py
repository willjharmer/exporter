from flask.ext.script import Manager, Command
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate, MigrateCommand
from faker import Faker

from app import AppFactory
from app.configs import Dev
import os

app = AppFactory.create(config=Dev)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

class WEATHER(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    colA = db.Column(db.String(128))
    colB = db.Column(db.String(128))
    colC = db.Column(db.String(128))

    def __init__(self, colA, colB, colC):
        self.colA = colA
        self.colB = colB
        self.colC = colC

class STATIONS(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    colA = db.Column(db.String(128))
    colB = db.Column(db.String(128))
    colC = db.Column(db.String(128))

class NCDC(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    colA = db.Column(db.String(128))
    colB = db.Column(db.String(128))
    colC = db.Column(db.String(128))


class Tests(Command):
    description = 'Runs Lettuce and Nose tests.'

    def run(self):
        lettuce_options = "--tag=Browser"
        nose_options = "--rednose --force-color"
        os.system('lettuce ' + lettuce_options)
        os.system('nosetests ' + nose_options)

manager.add_command("test", Tests())

class DataGen(Command):
    description = 'Populates the test database with some fake data.'

    def run(self):
        #fake = Faker()
        #fake.seed(4321)

        gen1 = TableA(colA="ran",colB="dom",colC="word")
        #gen2 = AnotherTableB(fake.word(),fake.word(),fake.word())
        #gen3 = DatatableC(fake.word(),fake.word(),fake.word())

        db.session.add(gen1)
        db.session.commit()

manager.add_command("gen_data", DataGen())

if __name__ == '__main__':
    manager.run()



