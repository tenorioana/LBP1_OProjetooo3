from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def chamahtml(name=None):
    return render_template('index.html', name=None)


def create_app():
    app = Flask(__name__)

    from views import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

if __name__ == '__main__':
    app.run(debug=True)