from flask import Flask, render_template, request
from collections import defaultdict
import random


app = Flask(__name__)


def get_random_hex_color():
    letters = "0123456789ABCDEF"
    color = "#"
    for _ in range(6):
        color += random.choice(letters)
    return f'"{color}"'


space_to_color = defaultdict(get_random_hex_color)


@app.route("/<space>")
def get_space(space):
    print('your space', space)
    print(request.url)
    return render_template('main.html', space=space)


@app.route("/<space>/color")
def get_color(space):
    return space_to_color[space]


@app.route("/<space>/upd")
def update_color(space):
    space_to_color[space] = get_random_hex_color()
    return 'Ok'


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=3000)