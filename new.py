from flask import Flask, jsonify 
import ser

app = Flask(__name__)

@app.route("/code/<string:n>")
def code(n):
    result = {
        "Country Name": n,
        "Telephone Code": ser.find_ans(n,"code")
    }
    return jsonify(result)

@app.route("/time/<string:n>")
def time(n):
    result = {
        "Country Name": n,
        "Time Zone": ser.find_ans(n,"time")
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
