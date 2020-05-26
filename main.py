import os
import yaml
from flask import Flask, render_template
app = Flask(__name__)

with open('info.yml') as f:
    info = yaml.load(f, Loader=yaml.FullLoader)

@app.route('/')
def main():
    return render_template('main.html', info=info)


# @app.route("/")
# def download_resume(path = None):
#     if path is None:
#         self.Error(400)
#     try:
#         return send_file(path, as_attachment=True)
#     except Exception as e:
#         self.log.exception(e)
#         self.Error(400)

# @app.route('/projects')
# def projects():
#     return render_template('projects.html', info=info)

# @app.route('/about')
# def about():
#     return render_template('about.html', info=info)


if __name__ == '__main__':
    app.run(debug=True)