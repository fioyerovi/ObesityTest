from flask import Flask, request, render_template
import joblib
import array as ar

app = Flask(__name__)
model = joblib.load('model_jlib')

@app.route('/')
def home():
    return render_template('index.html')
  

@app.route('/predict',methods=['POST'])
def predict():
    arrayPred = ar.array(0, range(20))
    genero = request.form["genero"]
    arrayPred[genero] = 1
    edad = request.form['edad']
    arrayPred[15] = edad
    famSobre = request.form['pre3']
    arrayPred[16] = famSobre
    altoCalo = request.form['pre4']
    arrayPred[17] = altoCalo
    snack = request.form['pre7']
    arrayPred[snack] = 1
    monitoreo = request.form['pre10']
    arrayPred[18] = monitoreo
    actividad = request.form['pre11']
    arrayPred[19] = actividad
    alcohol = request.form['pre13']
    arrayPred[alcohol] = 1
    transpo = request.form['pre14']
    arrayPred[transpo] = 1


    prediction = model.predict([arrayPred])
    return render_template('index.html', prediction_text=f'${prediction}')

if __name__ == "__main__":
    app.run()