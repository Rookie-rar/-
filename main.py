from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "李萌大帅B"

if __name__ == '__main__':
    app.run(debug=True)
