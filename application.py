import os
import logging
from flask import Flask, request, render_template, redirect, url_for
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)

app = application

# Setup basic logging
logging.basicConfig(level=logging.DEBUG)

# Route for the home page
@app.route('/')
def index():
    try:
        logging.debug('Redirecting to predict_datapoint')
        return redirect(url_for('predict_datapoint'))
    except Exception as e:
        logging.error(f"Error in index route: {e}")
        return str(e), 500

# Route for the favicon
@app.route('/favicon.ico')
def favicon():
    return '', 204

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        try:
            data = CustomData(
                gender=request.form.get('gender'),
                race_ethnicity=request.form.get('ethnicity'),
                parental_level_of_education=request.form.get('parental_level_of_education'),
                lunch=request.form.get('lunch'),
                test_preparation_course=request.form.get('test_preparation_course'),
                reading_score=float(request.form.get('reading_score')),
                writing_score=float(request.form.get('writing_score'))
            )

            pred_df = data.get_data_as_data_frame()
            logging.debug(f"Data received: {pred_df}")

            predict_pipeline = PredictPipeline()
            results = predict_pipeline.predict(pred_df)
            return render_template('home.html', results=results[0])
        except Exception as e:
            logging.error(f"Error in predict_datapoint route: {e}")
            return str(e), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
