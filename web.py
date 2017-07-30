import numpy as np

def insert_csv(data):
    import csv
    import uuid
    tuid = str(uuid.uuid1())
    with open("./logs/"+tuid+".csv", "a") as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(["sepalLength","sepalWidth","petalLength","petalWidth"])
        writer.writerow(data)
    return tuid

def predictIris(params):
    from sklearn.externals import joblib
    # load the model
    forest = joblib.load('./rfcParam.pkl') 
    # predict
    params = params.reshape(1,-1)
    pred = forest.predict(params)
    return pred

def getIrisName(irisId):
    if irisId == 0: return "Iris Setosa" 
    elif irisId == 1: return "Iris Versicolour" 
    elif irisId == 2: return "Iris Virginica"
    else: return "Error"

from flask import Flask, render_template, request, flash
from wtforms import Form, FloatField, SubmitField, validators, ValidationError

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'fda0e618-685c-11e7-bb40-fa163eb65161'

class IrisForm(Form):
    SepalLength = FloatField("Sepal Length in cm",
                     [validators.InputRequired("all parameters are required!"),
                     validators.NumberRange(min=0, max=10)])
    SepalWidth = FloatField("Sepal Width in cm",
                     [validators.InputRequired("all parameters are required!"),
                     validators.NumberRange(min=0, max=10)])
    PetalLength = FloatField("Petal Length in cm",
                     [validators.InputRequired("all parameters are required!"),
                     validators.NumberRange(min=0, max=10)])
    PetalWidth = FloatField("Petal Width in cm",
                     [validators.InputRequired("all parameters are required!"),
                     validators.NumberRange(min=0, max=10)])
    submit = SubmitField("Try")

@app.route('/irisPred', methods = ['GET', 'POST'])
def irisPred():
    form = IrisForm(request.form)
    if request.method == 'POST':
        if form.validate() == False:
            flash("You need all parameters")
            return render_template('irisPred.html', form = form)
        else:            
            SepalLength = float(request.form["SepalLength"])            
            SepalWidth = float(request.form["SepalWidth"])            
            PetalLength = float(request.form["PetalLength"])            
            PetalWidth = float(request.form["PetalWidth"])
            params = np.array([SepalLength, SepalWidth, PetalLength, PetalWidth])
            print(params)
            insert_csv(params)
            pred = predictIris(params)
            irisName = getIrisName(pred)
            
            return render_template('success.html', irisName=irisName)
    elif request.method == 'GET':
        return render_template('irisPred.html', form = form)

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
    
    
    
