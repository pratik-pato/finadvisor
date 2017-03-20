import flask
from flask import Flask
app = Flask(__name__)

@app.route('/app')
def home():
    return flask.render_template('login.html')


@app.route('/app/register',methods = ['GET','POST'])
def register():       
        return flask.render_template('register.html')

@app.route('/app/dumpdata',methods = ['GET','POST'])
def dump():
        if flask.request.method == 'POST':
            result = flask.request.form
            return flask.render_template('result.html',result = result)

if __name__ == '__main__':
    app.run(debug = True)