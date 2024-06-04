from main import create_app
from flask import Flask

app = Flask()

if __name__ == '__main__':
    app.run(debug=True)