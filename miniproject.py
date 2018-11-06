from flask import Flask
from flask import jsonify
from flask import request


app = Flask(__name__)

@app.route("/name",methods = ["GET"])
def name():
    return jsonify({
        "name": "Zengtian Deng"
    })

@app.route("/hello/<name>",methods = ["GET"])
def add_data(name):
    return jsonify({
        "message": "Hello there, {}".format(name)
    })

@app.route("/distance", methods = ["POST"])
def post_dist():
    dist = request.get_json()
    diff = []
    diff.append(dist["b"][0] - dist["a"][0])
    diff.append(dist["b"][1] - dist["a"][1])
    length = (diff[0]**2+diff[1]**2)**0.5
    cat = {"distance": length, **dist}
    return jsonify(cat)



if __name__ == "__main__":
    app.run(host="127.0.0.1")