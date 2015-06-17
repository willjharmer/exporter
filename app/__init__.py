from flask import Flask

class AppFactory():

    @staticmethod
    def create():

        app = Flask(__name__)

        @app.route('/')
        def index():
            return render_template('index.html')

        return app
