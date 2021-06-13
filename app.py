from flask import Flask, render_template, request
import pickle
import numpy as np

filename = 'score_linreg_model2.pkl'
model = pickle.load(open(filename,'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/prediction',methods=['POST'])
def prediction():
    overs = float(request.form['overs'])
    runs = int(request.form['runs'])
    wickets = int(request.form['wickets'])
    runs_last_5 = int(request.form['runs_last_5'])
    wickets_last_5 = int(request.form['wickets_last_5'])

    batting_side = request.form.get('batting', False)
    if batting_side=='Chennai Super Kings':
        batting_side = [1,0,0,0,0,0,0,0]
    elif batting_side=='Delhi Daredevils':
        batting_side = [0,1,0,0,0,0,0,0]
    elif batting_side=='Kings XI Punjab':
        batting_side = [0,0,1,0,0,0,0,0]
    elif batting_side=='Kolkata Knight Riders':
        batting_side = [0,0,0,1,0,0,0,0]
    elif batting_side=='Mumbai Indians':
        batting_side = [0,0,0,0,1,0,0,0]
    elif batting_side=='Rajasthan Royals':
        batting_side = [0,0,0,0,0,1,0,0]
    elif batting_side=='Royal Challengers Bangalore':
        batting_side = [0,0,0,0,0,0,1,0]
    elif batting_side=='Sunrisers Hyderabad':
        batting_side = [0,0,0,0,0,0,0,1]

    bowling_side = request.form.get('bowling', False)
    if bowling_side=='Chennai Super Kings':
        bowling_side = [1,0,0,0,0,0,0,0]
    elif bowling_side=='Delhi Daredevils':
        bowling_side = [0,1,0,0,0,0,0,0]
    elif bowling_side=='Kings XI Punjab':
        bowling_side = [0,0,1,0,0,0,0,0]
    elif bowling_side=='Kolkata Knight Riders':
        bowling_side = [0,0,0,1,0,0,0,0]
    elif bowling_side=='Mumbai Indians':
        bowling_side = [0,0,0,0,1,0,0,0]
    elif bowling_side=='Rajasthan Royals':
        bowling_side = [0,0,0,0,0,1,0,0]
    elif bowling_side=='Royal Challengers Bangalore':
        bowling_side = [0,0,0,0,0,0,1,0]
    elif bowling_side=='Sunrisers Hyderabad':
        bowling_side = [0,0,0,0,0,0,0,1]
    
    features = [runs,wickets,overs,wickets_last_5,runs_last_5]+batting_side+bowling_side
    features = np.array([features])

    prediction = int(model.predict(features)[0])

    return render_template('result.html',lower = prediction-10, upper = prediction+5)

if __name__ == '__main__':
	app.run(debug=True)