from flask import Flask,render_template,request
# from flask_cors import cross_origin
# from nltk.chat.util import Chat,reflections
import numpy  as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle
from sklearn.model_selection import RandomizedSearchCV 


app = Flask(__name__)
model = pickle.load(open("SBI.pkl", "rb"))
app.static_folder = 'static'
# model=joblib.load(open("SBI.pkl",'rb'))


@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/predict",methods=['GET','POST'])
def predict():
    if request.method=='POST':
        AGE=request.form["Age"]
        print(AGE)
        age=int(AGE)
    

        SEX=request.form["Sex"]
        print(SEX)
        if SEX== "Male":
            sex=1
        else:
            sex=0

        BMi=request.form.get("BMI")
        print(BMi)
        bmi=float(BMi)
        print(bmi)

        CHILDREN=request.form["Childrens"]
        children=int(CHILDREN)

        SMOKER=request.form['Smoker']
        print(SMOKER)
        if SMOKER== "Yes":
            smoker=1
        else:
            smoker=0
        # smoker=int(SMOKER)
        REGION=request.form["Region"]
        print(REGION)
        if REGION=="NorthEast":
            region=0
        elif(REGION=="NorthWest"):
            region=1
        elif(REGION=="SouthEast"):
            region=2
        elif(REGION=="SouthWest"):
            region=3
        else:
            REGION=="NO REGION"
       
        CHARGES=request.form["Charges"]
        charges=float(CHARGES)

        prediction=model.predict([[
            age, 
            sex,
            bmi, 
            children, 
            smoker, 
            region,
            charges
        ]])

        output=round(prediction[0],2)
        if output ==1:
            output="Eligible"
        else:
            output="Not Eligible"




        return render_template('index.html',prediction_text=" You are {} for Claim ".format(output))


    return render_template('index.html')

if __name__=="__main__":
    app.run(port=8000,debug=True)