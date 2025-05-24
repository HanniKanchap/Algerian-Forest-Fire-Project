import pickle
from sklearn.preprocessing import StandardScaler
from flask import Flask,request,jsonify,render_template

application = Flask(__name__)
app = application

## import ridge regressor and standard scaler pickle
ridgeModel = pickle.load(open("models/Ridge.pkl",'rb'))
standard_scaler =  pickle.load(open("models/scaler.pkl",'rb'))


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictData',methods = ['GET','POST'])
def predict():
    if request.method  == "POST":
        temp = float(request.form.get('Temperature', 0))  # Convert to float
        rh = float(request.form.get('RH', 0))  # Convert to float
        ws = float(request.form.get('Ws', 0))  # Convert to float
        rain = float(request.form.get('Rain', 0))  # Convert to float
        ffmc = float(request.form.get('FFMC', 0))  # Convert to float
        dmc = float(request.form.get('DMC', 0))  # Convert to float
        isi = float(request.form.get('ISI', 0))  # Convert to float
        classes = int(request.form.get('Classes', 0))  # Convert to integer
        region = float(request.form.get('Region', 0))  # Convert to string    
        data  = standard_scaler.transform([[temp,rh,ws,rain,ffmc,dmc,isi,classes,region]])
        result = ridgeModel.predict(data)
        return render_template('home.html',result = result[0])

    else:
        return render_template('home.html')

if __name__ == "__main__":
    app.run(host = '0.0.0.0')