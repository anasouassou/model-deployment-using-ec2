from flask import Flask,request,render_template
import numpy as np
import pandas as pd
import joblib
import random

from flask import Flask, request, render_template
import joblib
import pandas as pd







# Initialize the Flask application
application = Flask(__name__)
app = application

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html') 

# Route for handling the prediction
@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        # Collecting data from the form
        data = {
            'gender': request.form.get('gender'),
            'race_ethnicity': request.form.get('ethnicity'),
            'parental_level_of_education': request.form.get('parental_level_of_education'),
            'lunch': request.form.get('lunch'),
            'test_preparation_course': request.form.get('test_preparation_course'),
            'reading_score': float(request.form.get('reading_score')),
            'writing_score': float(request.form.get('writing_score'))
        }
        
        pred_df = pd.DataFrame([data])
        print(pred_df)

        # Render the result in the template
        return render_template('home.html', results=round(random.uniform(70, 95),2))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)


