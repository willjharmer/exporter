from flask import Flask, render_template
from hamlish_jinja import HamlishExtension
from flask_wtf import Form
from configs import Dev

class AppFactory():

    @staticmethod
    def create(config=Dev):

        app = Flask(__name__)
        app.config.from_object(config)

        app.jinja_env.add_extension(HamlishExtension)
        AppFactory.register_errorhandlers(app)

        @app.route('/')
        def index():
            return render_template('index.haml')

        return app

#def register_extensions(app):

#def register_blueprints(app):
    @staticmethod
    def register_errorhandlers(app):
        def render_error(e):
            return render_template('errors/{0}.haml'.format(e.code)), e.code

        for e in [404, 500]:
            app.errorhandler(e)(render_error)
