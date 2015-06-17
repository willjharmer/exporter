from flask import Flask
from configs import Dev

class AppFactory():

    @staticmethod
    def create(config=Dev):

        app = Flask(__name__)
        app.config.from_object(config)

        @app.route('/')
        def index():
            return render_template('index.html')

        return app
