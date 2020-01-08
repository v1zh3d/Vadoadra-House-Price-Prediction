import numpy as np
from flask import Flask, request, jsonify, render_template, url_for
import pickle
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
standard_x = StandardScaler()
model = pickle.load(open('vadodara_house_model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    standard_value = standard_x.fit_transform(final_features)
    prediction = model.predict(standard_x.transform(standard_value))

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Estimated House Price should be ₹ {}'.format(output))


@app.route('/predict_api', methods=['POST'])
def predict_api():
    '''
    For direct API calls through request
    '''
    data = request.get_json(force=True)
    standard_value = standard_x.fit_transform([np.array(list(data.values()))])
    prediction = model.predict(standard_x.transform(standard_value))

    output = prediction[0]
    return jsonify(output)


if __name__ == "__main__":
    app.run(debug=True)
