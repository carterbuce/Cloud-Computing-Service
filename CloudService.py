from flask import Flask, request, abort, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/reverse', methods=['POST'])
def reverse_string():
    if not request.json or 'string' not in request.json:
        abort(400)

    reversed_string = str(request.json['string'])[::-1]
    return jsonify({'reversed': reversed_string})


if __name__ == '__main__':
    app.run()
