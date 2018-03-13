from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    return "Hello world"

@app.route('/forward', methods=["GET"])
def fw():
    print("Going forward")
    return "Going forward"



@app.route('/speed/<id>', methods=["GET"])
def speed(id):
    print("Going speed",id)
    return "Going speed "+ id



app.run(debug=True)


