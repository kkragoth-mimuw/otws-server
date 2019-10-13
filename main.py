from flask import Flask, render_template, request, json

app = Flask(__name__)

votes = []


@app.route('/')
def main():
    return render_template("index.html")


def is_float(value):
    try:
        float(value)
        return True
    except:
        return False


@app.route('/vote', methods=['POST'])
def vote():
    _x = request.form['x']
    _y = request.form['y']
    _class = request.form['class']

    if is_float(_x) and is_float(_y):
        x = float(_x)
        y = float(_y)

        if 10 >= x >= -10 and 10 >= y >= -10:
            votes.append({
                "x": x,
                "y": y,
                "class": _class
            })
            return 'OK!'
        else:
            return 'Not in range'

    else:
        return 'Not floats!'


@app.route('/results')
def results():
    return json.dumps({"results": votes})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6969)
