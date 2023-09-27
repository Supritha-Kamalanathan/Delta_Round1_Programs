from flask import Flask

app = Flask(__name__)

count = 0

@app.route('/index')

def hello():
    global count
    count += 1
    return f'Hello World! You have requested this endpoint {count} times'

if __name__ == '__main__':
    app.run()
