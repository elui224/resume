import os
import yaml
from flask import Flask, render_template
app = Flask(__name__)

with open('info.yml') as f:
    info = yaml.load(f, Loader=yaml.FullLoader)

@app.route('/')
def main():
    return render_template('main.html', info=info)


if __name__ == '__main__':
    app.run(debug=True)