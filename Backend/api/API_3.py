from flask import Flask, jsonify

app = Flask(__name__)

count = 0

@app.route('/index')

def hello():
    global count
    count += 1
    response = {"response": "Hello World!", "times-requested": count}
    return jsonify(response)

if __name__ == '__main__':
    app.run()
