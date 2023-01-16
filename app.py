import pickle
from flask import Flask, request, render_template
#import joblib
import array as ar
import pandas as pd
import numpy as np


app = Flask(__name__)
#model = joblib.load('model_jlib')
model = pickle.load(open('model2.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')
  

@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method == "POST":
        arrayPred = ar.array("f", range(20))
        for i in range(0, 20):
            arrayPred[i] = 0
        genero = int(request.form.get("genero"))
        arrayPred[genero] = 1
        edad = int(request.form.get('edad'))
        arrayPred[15] = edad
        famSobre = int(request.form.get('pre3'))
        arrayPred[16] = famSobre
        altoCalo = int(request.form.get('pre4'))
        arrayPred[17] = altoCalo
        snack = int(request.form.get('pre7'))
        arrayPred[snack] = 1
        monitoreo = int(request.form.get('pre10'))
        arrayPred[18] = monitoreo
        actividad = int(request.form.get('pre11'))
        arrayPred[19] = actividad
        alcohol = int(request.form.get('pre13'))
        arrayPred[alcohol] = 1
        transpo = int(request.form.get('pre14'))
        arrayPred[transpo] = 1

        d2 = {'MTRANS_Automobile': [arrayPred[0]], 'MTRANS_Bike': [arrayPred[1]], 'MTRANS_Motorbike': [arrayPred[2]],
            'MTRANS_Public_Transportation': [arrayPred[3]],
            'MTRANS_Walking': [arrayPred[4]],
            'Gender_Female': [arrayPred[5]], 'Gender_Male': [arrayPred[6]],
            'CALC_Always': [arrayPred[7]], 'CALC_Frequently': [arrayPred[8]], 'CALC_Sometimes': [arrayPred[9]],
            'CALC_no': [arrayPred[10]],
            'CAEC_Always': [arrayPred[11]], 'CAEC_Frequently': [arrayPred[12]], 'CAEC_Sometimes': [arrayPred[13]],
            'CAEC_no': [arrayPred[14]],
            'Age': [arrayPred[15]], 'FHWO': [arrayPred[16]], 'FAVC': [arrayPred[17]], 'SCC': [arrayPred[18]],
            'FAF': [arrayPred[19]]} 

        
        df2 = pd.DataFrame(data=d2)


        prediction = model.predict(df2[:1])
        prediction = str(np.argmax(prediction))
        match prediction:
            case "0":
                return render_template('index.html', prediction_text='Insufficient_Weight')
            case "1":
                return render_template('index.html', prediction_text='Normal_Weight')
            case "2":
                return render_template('index.html', prediction_text='Overweight_Level_I')
            case "3":
                return render_template('index.html', prediction_text='Overweight_Level_II')
            case "4":
                return render_template('index.html', prediction_text='Obesity_Type_I')
            case "5":
                return render_template('index.html', prediction_text='Obesity_Type_II')
            case "6":
                return render_template('index.html', prediction_text='Obesity_Type_III')

if __name__ == "__main__":
    app.run()