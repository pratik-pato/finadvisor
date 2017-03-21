import src.sql as sql
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
            formData = []
            result = flask.request.form
            formData.append(result['userName'])
            formData.append(result['contact'])
            formData.append(result['firstName'])
            formData.append(result['middleName'])
            formData.append(result['lastName'])
            formData.append(result['password'])
            formData.append(result['email'])
            print formData
            if sql.consultantInsert(formData) == 1:
                return "<h1>ERROR IN DATA</h1>"
            #print formData[1]
            return flask.render_template('result.html',result = result)

if __name__ == '__main__':
    app.run(debug = True)