from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello flat!"

@app.route("/test")
def test():
    return "This is a test!"

if __name__ == "__main__":
    app.run()
