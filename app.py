from flask import Flask,render_template,request
import pickle

app=Flask(__name__)
model=pickle.load(open('studentmarks.pkl','rb'))



@app.route('/')
def index():
    result=' '
    return render_template('index.html',**locals())


@app.route('/predict',methods=['POST','GET'])
def predict():
    number_courses=int(request.form['number_courses'])
    time_study=float(request.form['time_study'])
    result= int(model.predict([[number_courses,time_study]])[0])
    

    return render_template('index.html',**locals())




if __name__=="__main__":
    app.run(debug=True)