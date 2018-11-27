from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Верфь кораблей для Кориолис RPG!'


if __name__ == '__main__':
    app.run()
