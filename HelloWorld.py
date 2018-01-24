from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<H1>Hello World python Flask </H1>"

if __name__ == "__main__":
    app.run()