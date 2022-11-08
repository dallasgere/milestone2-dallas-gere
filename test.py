import flask
from flask import request

app = flask.Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():

    if request.method == 'POST':
        username = request.form.get('username')
        comment = request.form.get('comment')
        return flask.redirect(flask.url_for('comment'))
    return flask.render_template('comment_form.html')

if __name__ == '__main__':
    app.run(debug=True)